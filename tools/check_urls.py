# /// script
# requires-python = ">=3.11"
# ///
"""Check that every page of the old (separate) doc sites still exists.

Reads the sitemap.xml of each old site (live, or a local copy) and checks that
the same path exists in the freshly built site/ (as a page or a redirect).

    uv run tools/check_urls.py            # after `just build`
    uv run tools/check_urls.py --live     # against the deployed site instead
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
BASE = "https://pymmcore-plus.github.io"
OLD_SITES = ["pymmcore-plus", "useq-schema", "pymmcore-widgets", "napari-micromanager"]
# the old sitemaps are archived here the first time they are fetched, because
# once the new site is deployed the old sitemaps are gone
ARCHIVE = ROOT / "tools" / "old_sitemaps"


def old_urls(site: str) -> list[str]:
    cached = ARCHIVE / f"{site}.xml"
    if not cached.exists():
        ARCHIVE.mkdir(exist_ok=True)
        with urllib.request.urlopen(f"{BASE}/{site}/sitemap.xml", timeout=30) as resp:
            cached.write_bytes(resp.read())
    return re.findall(r"<loc>(.*?)</loc>", cached.read_text(encoding="utf-8"))


def exists_locally(path: str) -> bool:
    target = SITE / path.strip("/")
    return (target / "index.html").exists() or target.is_file()


def exists_live(path: str) -> bool:
    try:
        with urllib.request.urlopen(BASE + path, timeout=30) as resp:
            return resp.status == 200
    except Exception:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--live", action="store_true", help="check the deployed site")
    ns = parser.parse_args()
    check = exists_live if ns.live else exists_locally

    missing = []
    total = 0
    for site in OLD_SITES:
        for url in old_urls(site):
            total += 1
            path = urlparse(url).path
            if not check(path):
                missing.append(path)
    for path in missing:
        print(f"MISSING {path}")
    print(f"{total - len(missing)}/{total} old URLs resolve")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
