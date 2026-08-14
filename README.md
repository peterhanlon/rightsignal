# RightSignal — the current state of AI, continuously adjudicated

This repository is the **public half** of [rightsignal.co.uk](https://rightsignal.co.uk):
the board data, the changelog, and the static site generator. The **private half**
([`rightsignal-pipeline`](https://github.com/peterhanlon/rightsignal-pipeline)) is the
autonomous editorial pipeline that ingests releases, benchmarks and papers daily,
adjudicates each title against published criteria, and commits every change here.

Every change to the board is a commit in this repository — the full judgment
record is public and auditable, back to day one.

> **Seed data notice:** the current picks are illustrative placeholders (flagged
> `provisional: true`). They must be reviewed and confirmed before launch.

## Layout

| Path | What it is |
|---|---|
| `data/site.yaml` | Site-wide config (name, tagline, category order) |
| `data/slots/*.yaml` | One file per **slot** — a title like "Best open-weight TTS": current pick, criteria, challengers, full lineage |
| `changelog/*.md` | One file per changelog event (`changed` / `challenged` / `held` / `added` / `retired` / `snapshot`), YAML frontmatter + Markdown body |
| `snapshots/YYYY-MM/` | Monthly frozen copies of `data/slots/` plus `meta.yaml` — the historical record |
| `site/` | Static site generator (Python + Jinja2) and templates |
| `.github/workflows/deploy.yml` | Builds and deploys to GitHub Pages on every push to `main` |
| `.github/workflows/veto-window.yml` | Auto-merges pipeline `title-change` PRs after a 24h human veto window |

## Building locally

```sh
pip install -r requirements.txt
python site/build.py            # writes dist/
python -m http.server -d dist   # preview at http://localhost:8000
```

## How changes land

- **`held` / `challenged`** entries are committed directly to `main` by the pipeline.
- **`changed`** entries (a title changing hands) arrive as a pull request labelled
  `title-change`. It auto-merges after 24 hours unless a human closes it — closing
  the PR *is* the veto.

## One-time setup (deployment)

1. Make this repository **public** (free Pages + unlimited Actions minutes, and
   the public audit trail is the point).
2. Repo → Settings → Pages → Source: **GitHub Actions**.
3. Settings → Pages → Custom domain: `rightsignal.co.uk` (and verify the domain
   under org/user Settings → Pages to prevent takeover).
4. DNS at the registrar:
   - `A` records for the apex → `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153`, `185.199.111.153`
   - `CNAME` for `www` → `peterhanlon.github.io`
5. In `rightsignal-pipeline`, add a fine-grained PAT scoped to this repo as the
   `PUBLIC_REPO_TOKEN` secret (contents + pull-requests: read/write) so the
   pipeline can push data commits and open title-change PRs.

Board data is licensed CC BY 4.0.
