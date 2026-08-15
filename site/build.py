#!/usr/bin/env python3
"""Static site generator for rightsignal.co.uk.

Reads the board data (data/slots/*.yaml), the changelog (changelog/*.md) and
frozen snapshots (snapshots/YYYY-MM/), renders the site into dist/.

Usage: python site/build.py [--out dist]
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import sys
from email.utils import format_datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
DATA_DIR = ROOT / "data"
CHANGELOG_DIR = ROOT / "changelog"
SNAPSHOTS_DIR = ROOT / "snapshots"

ENTRY_TYPES = ("changed", "challenged", "held", "added", "retired", "snapshot", "milestone")


def as_date(value) -> dt.date | None:
    if value is None or value == "":
        return None
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def assign_bars(slots: list[dict], today: dt.date) -> None:
    """Reign bar width = sqrt(days)/sqrt(longest reign), min 4% (design spec).
    A title held for <= 3 days renders as 'new titleholder' (magenta)."""
    if not slots:
        return
    max_days = max(s["reign_days"] or 1 for s in slots)
    for s in slots:
        days = s["reign_days"] or 1
        s["bar_pct"] = max(4, round((days**0.5) / (max_days**0.5) * 100))
        s["is_new"] = days <= 3


def load_slot(path: Path, today: dt.date) -> dict:
    slot = yaml.safe_load(path.read_text())
    slot["since"] = as_date(slot.get("since"))
    slot["last_reviewed"] = as_date(slot.get("last_reviewed"))
    # reign_days = elapsed days (a count); reign_day = ordinal ("day 1" on launch day)
    slot["reign_days"] = (today - slot["since"]).days if slot["since"] else None
    slot["reign_day"] = slot["reign_days"] + 1 if slot["reign_days"] is not None else None

    # Lineage: past holders plus the current pick, with widths proportional to
    # reign length (clamped so short reigns stay visible).
    history = []
    for h in slot.get("history") or []:
        history.append(
            {
                "name": h["name"],
                "from": as_date(h.get("from")),
                "to": as_date(h.get("to")),
            }
        )
    slot["history"] = history

    spans = []
    for h in history:
        days = (h["to"] - h["from"]).days if h["from"] and h["to"] else 30
        spans.append({"name": h["name"], "days": max(days, 1), "current": False})
    spans.append({"name": slot["pick"]["name"], "days": max(slot["reign_days"] or 1, 1), "current": True})
    total = sum(s["days"] for s in spans)
    for s in spans:
        s["pct"] = max(round(100 * s["days"] / total), 4)
    slot["lineage"] = spans
    return slot


def parse_entry(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---"):
        raise ValueError(f"{path}: changelog entries need YAML frontmatter")
    _, fm, body = text.split("---", 2)
    entry = yaml.safe_load(fm)
    if entry.get("type") not in ENTRY_TYPES:
        raise ValueError(f"{path}: unknown entry type {entry.get('type')!r}")
    entry["date"] = as_date(entry["date"])
    entry["body_html"] = markdown.markdown(body.strip())
    entry["path"] = path
    entry["id"] = path.stem
    return entry


def load_snapshots(today: dt.date) -> list[dict]:
    snapshots = []
    if not SNAPSHOTS_DIR.exists():
        return snapshots
    for snap_dir in sorted(SNAPSHOTS_DIR.iterdir(), reverse=True):
        if not snap_dir.is_dir():
            continue
        meta_path = snap_dir / "meta.yaml"
        meta = yaml.safe_load(meta_path.read_text()) if meta_path.exists() else {}
        frozen = as_date(meta.get("frozen")) or today
        slots = [
            load_slot(p, frozen)
            for p in sorted(snap_dir.glob("*.yaml"))
            if p.name != "meta.yaml"
        ]
        assign_bars(slots, frozen)
        snapshots.append(
            {
                "key": snap_dir.name,  # YYYY-MM
                "label": dt.date.fromisoformat(snap_dir.name + "-01").strftime("%B %Y"),
                "frozen": as_date(meta.get("frozen")),
                "changes": meta.get("changes", 0),
                "slots": slots,
            }
        )
    return snapshots


def build(out_dir: Path) -> None:
    today = dt.date.today()
    site = yaml.safe_load((DATA_DIR / "site.yaml").read_text())

    slots = [load_slot(p, today) for p in sorted((DATA_DIR / "slots").glob("*.yaml"))]
    assign_bars(slots, today)
    slots_by_key = {s["slot"]: s for s in slots}

    entries = sorted(
        (parse_entry(p) for p in sorted(CHANGELOG_DIR.glob("*.md"))),
        key=lambda e: (e["date"], e["id"]),
        reverse=True,
    )
    for entry in entries:
        entry["slot_title"] = slots_by_key.get(entry.get("slot"), {}).get("title")
        plain = re.sub(r"<[^>]+>", " ", entry["body_html"])
        plain = re.sub(r"\s+", " ", plain).strip()
        first = re.split(r"(?<=[.!?])\s+", plain)[0] if plain else ""
        entry["teaser"] = first if len(first) <= 140 else first[:137] + "…"

    categories = []
    for cat in site["categories"]:
        cat_slots = sorted(
            (s for s in slots if s["category"] == cat["key"]),
            key=lambda s: s.get("rank", 99),
        )
        if cat_slots:
            categories.append({**cat, "slots": cat_slots})

    snapshots = load_snapshots(today)

    radar = []
    radar_path = DATA_DIR / "radar.yaml"
    if radar_path.exists():
        for item in yaml.safe_load(radar_path.read_text())["radar"]:
            item["released"] = as_date(item.get("released"))
            item["slug"] = re.sub(r"[^a-z0-9]+", "-", item["name"].lower()).strip("-")
            radar.append(item)
        radar.sort(key=lambda i: i["released"], reverse=True)

    env = Environment(
        loader=FileSystemLoader(SITE_DIR / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["dmy"] = lambda d: d.strftime("%-d %b %Y") if d else ""
    # Lowercase only the first character — keeps acronyms like "LLM" intact.
    env.filters["lc_first"] = lambda s: s[:1].lower() + s[1:] if s else s
    env.filters["lc_first_cap"] = lambda s: s[:1].upper() + s[1:] if s else s
    # Split prose into sentence bullets (used on detail pages).
    env.filters["sentences"] = lambda s: [x.strip() for x in re.split(r"(?<=[.!?])\s+", s or "") if x.strip()]

    # Lead story: the hottest actual news — the newest title change/challenge,
    # or the freshest radar arrival if that's more recent. Never site meta.
    news = next(
        (e for e in entries if e["type"] in ("changed", "challenged") and e.get("slot")),
        None,
    )
    lead, lead_slot = None, None
    if radar and (news is None or radar[0]["released"] >= news["date"]):
        item = radar[0]
        lead = {
            "type": "unverified",
            "title": f'{item["name"]}: a new contender for {item["target"]}',
            "body_html": markdown.markdown(item["note"]),
            "href": "#radar",
            "link_text": "See the radar →",
        }
    elif news:
        lead = {**news, "href": "#changelog", "link_text": "Read the adjudication →"}
        lead_slot = slots_by_key.get(news.get("slot"))

    # Cache-buster: the stylesheet URL changes whenever its content does, so a
    # cached CSS can never be paired with newer HTML.
    css_v = hashlib.sha256((SITE_DIR / "static" / "style.css").read_bytes()).hexdigest()[:8]

    ctx = {
        "site": site,
        "css_v": css_v,
        "today": today,
        "last_review": max((s["last_reviewed"] for s in slots if s["last_reviewed"]), default=today),
        "entries": entries,
        "snapshots": snapshots,
        "slots_count": len(slots),
        "lead": lead,
        "lead_slot": lead_slot,
        "radar": radar,
    }

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    (out_dir / "index.html").write_text(
        env.get_template("home.html").render(categories=categories, slots=slots, **ctx)
    )
    for page, template in (
        ("picks", "picks.html"), ("radar", "radar.html"), ("changes", "changes.html"),
        ("history", "history.html"), ("method", "method.html"),
    ):
        page_dir = out_dir / page
        page_dir.mkdir(parents=True)
        (page_dir / "index.html").write_text(
            env.get_template(template).render(categories=categories, slots=slots, **ctx)
        )

    for slot in slots:
        slot_entries = [e for e in entries if e.get("slot") == slot["slot"]]
        # Detail-page derivations, all from recorded data:
        defences = sum(
            1 for e in slot_entries
            if e["type"] == "challenged" and e["date"] >= slot["since"]
        )
        past_reigns = sum(1 for h in slot["history"] if h["name"] == slot["pick"]["name"])
        by_new = {e.get("new"): e for e in slot_entries if e.get("new")}
        hist_rows = []
        for h in reversed(slot["history"]):  # newest first
            e = by_new.get(h["name"])
            hist_rows.append({**h, "days": (h["to"] - h["from"]).days,
                              "teaser": e["teaser"] if e else ""})
        evidence, seen = [], set()
        for e in slot_entries:
            for src in e.get("sources", []):
                if src not in seen:
                    seen.add(src)
                    evidence.append(src)
        page_dir = out_dir / "slots" / slot["slot"]
        page_dir.mkdir(parents=True)
        (page_dir / "index.html").write_text(
            env.get_template("slot.html").render(
                slot=slot, slot_entries=slot_entries, defences=defences,
                past_reigns=past_reigns, hist_rows=hist_rows,
                evidence=evidence[:8], categories=categories, **ctx
            )
        )

    for snap in snapshots:
        snap_dir = out_dir / "snapshots" / snap["key"]
        snap_dir.mkdir(parents=True)
        snap_categories = [
            {**cat, "slots": [s for s in snap["slots"] if s["category"] == cat["key"]]}
            for cat in site["categories"]
        ]
        (snap_dir / "index.html").write_text(
            env.get_template("snapshot.html").render(
                snapshot=snap, categories=[c for c in snap_categories if c["slots"]], **ctx
            )
        )

    # RSS feed of the changelog.
    feed_items = []
    for e in entries[:50]:
        pub = dt.datetime.combine(e["date"], dt.time(6, 0), tzinfo=dt.timezone.utc)
        feed_items.append({**e, "rfc822": format_datetime(pub)})
    (out_dir / "feed.xml").write_text(
        env.get_template("feed.xml").render(items=feed_items, **ctx)
    )

    static_src = SITE_DIR / "static"
    if static_src.exists():
        shutil.copytree(static_src, out_dir / "static")

    print(f"Built {len(slots)} slots, {len(entries)} changelog entries, "
          f"{len(snapshots)} snapshots -> {out_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(ROOT / "dist"), help="output directory")
    args = parser.parse_args()
    build(Path(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
