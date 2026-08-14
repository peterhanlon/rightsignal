#!/usr/bin/env python3
"""Static site generator for rightsignal.co.uk.

Reads the board data (data/slots/*.yaml), the changelog (changelog/*.md) and
frozen snapshots (snapshots/YYYY-MM/), renders the site into dist/.

Usage: python site/build.py [--out dist]
"""
from __future__ import annotations

import argparse
import datetime as dt
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

ENTRY_TYPES = ("changed", "challenged", "held", "added", "retired", "snapshot")


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
    slot["reign_days"] = (today - slot["since"]).days + 1 if slot["since"] else None

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

    categories = []
    for cat in site["categories"]:
        cat_slots = [s for s in slots if s["category"] == cat["key"]]
        if cat_slots:
            categories.append({**cat, "slots": cat_slots})

    snapshots = load_snapshots(today)

    env = Environment(
        loader=FileSystemLoader(SITE_DIR / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["dmy"] = lambda d: d.strftime("%-d %b %Y") if d else ""

    # Lead story: the most recent changed/added/challenged entry, plus the slot
    # it refers to (for the day-of-reign numeral).
    lead = next(
        (e for e in entries if e["type"] in ("changed", "added", "challenged")), None
    )
    lead_slot = slots_by_key.get(lead.get("slot")) if lead else None

    ctx = {
        "site": site,
        "today": today,
        "entries": entries,
        "snapshots": snapshots,
        "slots_count": len(slots),
        "lead": lead,
        "lead_slot": lead_slot,
    }

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(categories=categories, slots=slots, **ctx)
    )

    for slot in slots:
        slot_entries = [e for e in entries if e.get("slot") == slot["slot"]]
        page_dir = out_dir / "slots" / slot["slot"]
        page_dir.mkdir(parents=True)
        (page_dir / "index.html").write_text(
            env.get_template("slot.html").render(slot=slot, slot_entries=slot_entries, **ctx)
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
