"""Griffe extension for the unified docs: tidy what griffe and griffe-fieldz produce.

- griffe-fieldz falls back to a field's ``default_factory.__doc__`` for fields
  without a description (a ``list`` field gets "Built-in mutable sequence..."),
  uses a dataclass' auto-generated ``__doc__`` (its signature, with reprs) as the
  class description, and reports types as ``ForwardRef('...')`` in modules using
  ``from __future__ import annotations``.  Undo all three.
- Drop the attribute-scope labels ("class-attribute", "instance-attribute",
  "module-attribute"): the heading already says "attribute".
- Drop ``Kwargs`` TypedDicts nested in classes (useq defines them for typing only).
- Drop undocumented instance attributes of the Qt packages' classes: those are
  child widgets (``self.btn = QPushButton()``), not API.
"""

from __future__ import annotations

import builtins
import inspect
import re
import types
from typing import TYPE_CHECKING, Any

from griffe import (
    DocstringSectionAttributes,
    DocstringSectionParameters,
    DocstringSectionText,
    Extension,
)

if TYPE_CHECKING:
    from griffe import Class, Module, Object

BUILTIN_DOCS = {
    inspect.cleandoc(t.__doc__)
    for t in (*vars(builtins).values(), types.MappingProxyType)
    if isinstance(t, type) and t.__doc__
}
SCOPE_LABELS = {"class-attribute", "instance-attribute", "module-attribute"}
QT_PACKAGES = {"pymmcore_widgets", "pymmcore_gui"}
FORWARD_REF = re.compile(r"ForwardRef\('([^']*)'")


class TidyDocs(Extension):
    def on_class(self, *, cls: Class, **kwargs: Any) -> None:
        if cls.docstring:
            sections = cls.docstring.parsed
            # a dataclass' auto __doc__ ("Name(field: type = default, ...)")
            if (
                sections
                and isinstance(sections[0], DocstringSectionText)
                and sections[0].value.startswith(f"{cls.name}(")
            ):
                del sections[0]
            for section in sections:
                if isinstance(
                    section, (DocstringSectionAttributes, DocstringSectionParameters)
                ):
                    for item in section.value:
                        _tidy_item(cls, item)

        if "Kwargs" in cls.members and cls.members["Kwargs"].is_class:
            del cls.members["Kwargs"]

    def on_package(self, *, pkg: Module, **kwargs: Any) -> None:
        # after the whole tree is built: instance attributes are only known then
        _tidy_tree(pkg, set(), qt=pkg.name in QT_PACKAGES)


def _tidy_item(cls: Class, item: Any) -> None:
    if item.description and item.description.strip() in BUILTIN_DOCS:
        item.description = ""
    if item.annotation is not None and (m := FORWARD_REF.search(str(item.annotation))):
        # prefer the member's own (static, cross-referenced) annotation
        member = cls.members.get(item.name)
        static = getattr(member, "annotation", None) if member else None
        item.annotation = static or m.group(1)


def _tidy_tree(obj: Object, seen: set[str], *, qt: bool) -> None:
    for name, member in list(obj.members.items()):
        if member.is_alias or member.path in seen:
            continue
        seen.add(member.path)
        if (
            qt
            and obj.is_class
            and member.is_attribute
            and member.labels == {"instance-attribute"}
            and not member.docstring
        ):
            del obj.members[name]
            continue
        member.labels -= SCOPE_LABELS
        if member.is_class or member.is_module:
            _tidy_tree(member, seen, qt=qt)
