"""Python-Markdown extension for the unified pymmcore-plus docs.

zensical has no page hooks, but it renders pages with Python-Markdown, so a
postprocessor sees each page's final HTML.  We use that to:

1. Register *re-export* paths as secondary autorefs anchors.  tools/api.py
   renders each object once, at its highest-level public name, and writes
   build/aliases.json (`{"pymmcore_plus.core.Device": "pymmcore_plus.Device"}`).
   Here, every rendered heading id under a preferred path is also registered
   under each alias path, so `[x][pymmcore_plus.core.Device.getPropertyObject]`
   resolves to the `pymmcore_plus.Device.getPropertyObject` heading.
2. Decorate "**Why Override?**" paragraphs in CMMCorePlus docstrings.
3. Relabel "Attributes" as "Keys" on the metadata (TypedDict) reference page.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from functools import cache
from pathlib import Path
from typing import Any

from markdown import Extension, Markdown
from markdown.postprocessors import Postprocessor

ALIASES = Path(__file__).resolve().parent.parent / "build" / "aliases.json"
_ID = re.compile(r'\bid="([A-Za-z_][\w.]*)"')
WHY = "<strong>Why Override?</strong>"
WHY_HTML = (
    '<span class="pymm-why-override" title="Overridden by pymmcore-plus">'
    '<span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" '
    'viewBox="0 0 24 24"><path d="M20 14h-6v6h-4v-6H4v-4h6V4h4v6h6v4Z"/></svg>'
    f"</span>{WHY}</span>"
)


@cache
def _reverse_aliases() -> dict[str, tuple[str, ...]]:
    """Map preferred path -> alias paths."""
    if not ALIASES.exists():
        return {}
    reverse: dict[str, list[str]] = defaultdict(list)
    for alias, preferred in json.loads(ALIASES.read_text(encoding="utf-8")).items():
        reverse[preferred].append(alias)
    return {k: tuple(v) for k, v in reverse.items()}


def _current_page() -> Any:
    try:
        from zensical.extensions.autorefs import get_autorefs_store
    except ImportError:  # not running under zensical
        return None, None
    store = get_autorefs_store()
    return store, store.current_page


class PymmPostprocessor(Postprocessor):
    def run(self, text: str) -> str:
        store, page = _current_page()
        if page is None:
            return text
        if reverse := _reverse_aliases():
            for anchor in set(_ID.findall(text)):
                parts = anchor.split(".")
                for i in range(len(parts), 0, -1):
                    if aliases := reverse.get(".".join(parts[:i])):
                        rest = ".".join(parts[i:])
                        for alias in aliases:
                            ident = f"{alias}.{rest}" if rest else alias
                            store.register_anchor(page, ident, anchor, primary=False)
                        break
        if WHY in text:  # idempotent: mkdocstrings nests Markdown conversions
            text = re.sub(r"(?<!</span>)" + re.escape(WHY), WHY_HTML, text)
        src = str(getattr(page, "file", "") or getattr(page, "url", ""))
        if "pymmcore_plus/metadata" in src or "pymmcore_plus/metadata" in page.url:
            text = text.replace("<th>Attributes:</th>", "<th>Keys:</th>")
            text = re.sub(
                r"(<p><span class=\"doc-section-title\">)Attributes:", r"\1Keys:", text
            )
        return text


class PymmExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        # after raw HTML (incl. mkdocstrings output) is restored (priority 30)
        md.postprocessors.register(PymmPostprocessor(md), "pymm", 5)


def makeExtension(**kwargs: Any) -> PymmExtension:
    return PymmExtension(**kwargs)
