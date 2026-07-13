# Copyright 2026 Anthropic, PBC
# Copyright 2026 Learning Commons
# SPDX-License-Identifier: Apache-2.0

"""Shared-content helpers used by all artifact renderers.

The material-source JSON has a `shared` block holding every piece of content that appears in more
than one artifact (standard, anchor task, problems, exit ticket, look-fors, vocabulary,
misconceptions, sentence supports). Renderers expand it via `expand_from_shared`, so shared
content is written once and can never drift between artifacts.
"""
from __future__ import annotations

import re

# ---- render-time print-safety repair ---------------------------------------------------
# Two failure classes survive prompt instructions and are repaired structurally instead:
# (1) markdown pipe tables drawn inside prose fields print as literal '|' rows — convert
#     them to real `table` blocks; (2) the ■ unknown-number symbol appearing in an artifact
#     with no defining sentence in THAT artifact (look-fors carry ■ into the observation
#     sheet via from_shared, where the model writes no prose) — append the skill's standard
#     definition line to the first section that uses it.

_PIPE_LINE = re.compile(r"[^|\n]*\|[^|\n]+\|")            # a line with >=2 pipe chars
_SEP_LINE = re.compile(r"^\s*\|?[\s:|\-]+\|?\s*$")        # |---|:---| separator row
UNKNOWN_SYMBOL = "■"
_UNKNOWN_DEFINED = re.compile(
    r"(use|using|write|stands for|symbol|means)[^.]{0,50}■"
    r"|■[^.]{0,50}(for the|stands for|means|is the|if you need)", re.IGNORECASE)


def _parse_pipe_rows(lines: list[str]) -> list[list[str]]:
    rows = []
    for ln in lines:
        if _SEP_LINE.match(ln):
            continue
        rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
    width = max((len(r) for r in rows), default=0)
    return [r + [""] * (width - len(r)) for r in rows]


_INLINE_SEP = re.compile(r"\|\s*:?-{2,}")  # an inline |--- separator (table collapsed to one line)
_BULLET_LINE = re.compile(r"^\s*(?:[•▪‣◦]|[-–])\s+")

# Enumerated sub-parts written mid-prose — "… from Task 1: (a) Predict … (b) Describe …" —
# read as a wall of text. Insert a line break before each "(a)"/"(1)" marker that follows
# sentence-ending punctuation, so every sub-part starts on its own line. Both renderers
# preserve single newlines as line breaks.
_ENUM_MIDPROSE = re.compile(r"(?<=[.!?:;])[ \t]+(?=\((?:[a-h]|\d{1,2})\)\s)")

# Standards bodies write sub-parts as "A. Describe ... B. Describe ..." mid-prose; a verbatim
# standard then renders as a wall of text. Break before each capital-letter marker -- but only
# when the text carries a real enumeration (both "A." and "B." present after sentence ends),
# so initials like "Emmett J. Scott" never trigger it.
_CAP_MARKER = re.compile(r"(?<=[.?])[ \t]+(?=([A-H])\.\s+[A-Z])")


def _repair_cap_subparts(text: str) -> str:
    letters = {m.group(1) for m in _CAP_MARKER.finditer(text)}
    if not {"A", "B"} <= letters:
        return text
    return _CAP_MARKER.sub("\n", text)



def _repair_enum_breaks(blk: dict) -> list[dict]:
    """Put mid-prose enumerated sub-parts ('(a) …', '(2) …') on their own lines."""
    if blk.get("type") == "group":
        return [dict(blk, blocks=[rb for b in blk.get("blocks", [])
                                  for rb in _repair_enum_breaks(b)])]
    if blk.get("type") == "columns":
        return [dict(blk,
                     left=[rb for b in blk.get("left", []) for rb in _repair_enum_breaks(b)],
                     right=[rb for b in blk.get("right", []) for rb in _repair_enum_breaks(b)])]
    if blk.get("type") in ("paragraph", "labeled", "callout") and isinstance(blk.get("text"), str):
        fixed = _repair_cap_subparts(_ENUM_MIDPROSE.sub("\n", blk["text"]))
        if fixed != blk["text"]:
            return [dict(blk, text=fixed)]
    return [blk]


def _repair_inline_bullets(blk: dict) -> list[dict]:
    """Split prose containing bullet-marked lines ('• item') into prose + bullets blocks.
    A paragraph renders newlines as spaces, so bullets written inside a text string run
    together into one unreadable line."""
    if blk.get("type") == "group":
        return [dict(blk, blocks=[rb for b in blk.get("blocks", [])
                                  for rb in _repair_inline_bullets(b)])]
    if blk.get("type") == "columns":
        return [dict(blk,
                     left=[rb for b in blk.get("left", []) for rb in _repair_inline_bullets(b)],
                     right=[rb for b in blk.get("right", []) for rb in _repair_inline_bullets(b)])]
    if blk.get("type") not in ("paragraph", "labeled") or not isinstance(blk.get("text"), str) \
            or "\n" not in blk["text"]:
        return [blk]
    lines = blk["text"].split("\n")
    if not any(_BULLET_LINE.match(ln) for ln in lines):
        return [blk]
    out: list[dict] = []
    buf: list[str] = []
    items: list[str] = []
    first = True

    def flush_text():
        nonlocal first
        t = "\n".join(buf).strip()
        if t:
            out.append(dict(blk, text=t) if first else {"type": "paragraph", "text": t})
            first = False
        buf.clear()

    def flush_items():
        nonlocal first
        if items:
            if first and blk.get("type") == "labeled" and blk.get("label"):
                # The block opens with bullets — keep its label as a lead-in line
                # instead of silently dropping it.
                out.append({"type": "labeled", "label": blk["label"], "text": ""})
            out.append({"type": "list", "items": list(items)})
            first = False
            items.clear()

    for ln in lines:
        if _BULLET_LINE.match(ln):
            flush_text()
            items.append(_BULLET_LINE.sub("", ln, count=1).strip())
        elif ln.strip():
            flush_items()
            buf.append(ln)
        else:
            buf.append(ln)  # blank line — stays in whichever prose run is open
    flush_items()
    flush_text()
    return out or [blk]


def _repair_pipe_tables(blk: dict) -> list[dict]:
    """Split a prose block containing a markdown pipe-table run into prose + table blocks."""
    if blk.get("type") == "group":
        return [dict(blk, blocks=[rb for b in blk.get("blocks", [])
                                  for rb in _repair_pipe_tables(b)])]
    if blk.get("type") == "columns":
        return [dict(blk,
                     left=[rb for b in blk.get("left", []) for rb in _repair_pipe_tables(b)],
                     right=[rb for b in blk.get("right", []) for rb in _repair_pipe_tables(b)])]
    if btype(blk) in ("list", "checklist"):
        # A pipe table inside a bullet item: split the list around it and lift the table out.
        out: list[dict] = []
        cur: list = []
        for item in blk.get("items", []):
            if isinstance(item, str) and _INLINE_SEP.search(item):
                pieces = _repair_pipe_tables({"type": "paragraph", "text": item})
                if any(p.get("type") == "table" for p in pieces):
                    if cur:
                        out.append(dict(blk, items=cur))
                        cur = []
                    out.extend(pieces)
                    continue
            cur.append(item)
        if cur:
            out.append(dict(blk, items=cur))
        return out or [blk]
    if blk.get("type") not in ("paragraph", "labeled", "callout") \
            or not isinstance(blk.get("text"), str):
        return [blk]
    text = blk["text"]
    if "\n" not in text and _INLINE_SEP.search(text):
        # Table collapsed onto one line — restore row boundaries ("| |" marks a row break).
        text = re.sub(r"\|\s+\|", "|\n|", text)
        blk = dict(blk, text=text)
    lines = blk["text"].split("\n")
    if any(_INLINE_SEP.search(ln) for ln in lines):
        # Prose sharing a line with a table row would be swallowed into the table —
        # split "intro text: | a | b |" and "| x | y | trailing text" onto separate lines.
        norm: list[str] = []
        for ln in lines:
            m = re.match(r"^([^|]*[^|\s])\s*(\|.+\|)\s*$", ln)
            if m and not _SEP_LINE.match(ln):
                norm += [m.group(1), m.group(2)]
                continue
            m = re.match(r"^\s*(\|.+\|)\s*([^|]+)$", ln)
            if m and not _SEP_LINE.match(ln):
                norm += [m.group(1), m.group(2)]
                continue
            norm.append(ln)
        lines = norm
    out: list[dict] = []
    buf: list[str] = []
    i, first = 0, True

    def flush():
        nonlocal first
        t = "\n".join(buf).strip()
        if t:
            out.append(dict(blk, text=t) if first else {"type": "paragraph", "text": t})
            first = False
        buf.clear()

    while i < len(lines):
        if _PIPE_LINE.search(lines[i]):
            j = i
            while j < len(lines) and (_PIPE_LINE.search(lines[j]) or _SEP_LINE.match(lines[j])):
                j += 1
            if sum(1 for k in range(i, j) if not _SEP_LINE.match(lines[k])) >= 2:
                flush()
                rows = _parse_pipe_rows(lines[i:j])
                out.append({"type": "table", "headers": rows[0],
                            "rows": rows[1:] or [[""] * len(rows[0])]})
                first = False
                i = j
                continue
        buf.append(lines[i])
        i += 1
    flush()
    return out or [blk]


def _doc_text(sections: list[dict]) -> str:
    parts: list[str] = []

    def walk(v):
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif isinstance(v, dict):
            for x in v.values():
                walk(x)

    walk(sections)
    return "\n".join(parts)



# Keys in `shared` that are document/identity metadata, never expanded as content blocks.
_IDENTITY_KEYS = {"grade", "subject", "duration", "curriculum", "standard_code",
                  "standard_text", "prerequisite_standard", "smps"}


def _is_block(v) -> bool:
    return isinstance(v, dict) and ("type" in v or "blocks" in v)


def _as_blocks(v) -> list[dict]:
    """Coerce a shared-registry value into renderer blocks. Accepts a block dict, a list of
    block dicts, a typeless dict carrying the text/label/items field shapes (the schema's
    stable contract — a `{label, text}` value renders as a labeled block, never as its
    Python repr), or anything else (-> a single paragraph)."""
    if v is None or v == "":
        return []
    if _is_block(v):
        return [v]
    if isinstance(v, dict) and v.get("items"):
        return [{"type": "list", **{k: v[k] for k in ("label", "items") if k in v}}]
    if isinstance(v, dict) and v.get("text"):
        btype = "labeled" if v.get("label") else "paragraph"
        return [{"type": btype, **{k: v[k] for k in ("label", "text") if k in v}}]
    if isinstance(v, list) and v and all(_is_block(x) for x in v):
        return list(v)
    if isinstance(v, list):
        return [{"type": "list", "items": [str(x) for x in v]}]
    return [{"type": "paragraph", "text": str(v)}]


def _facet_text(v) -> str:
    """Flatten a plain facet (string / paragraph / list blocks) to text, or '' if it
    contains richer blocks that should render as-is."""
    blocks = _as_blocks(v)
    if not blocks or not all(b.get("type") in ("paragraph", "list") for b in blocks):
        return ""
    return "\n".join(b.get("text", "") if b.get("type") == "paragraph"
                     else "\n".join(f"- {it}" for it in b.get("items", []))
                     for b in blocks)


def _faceted(val: dict, audience: str) -> list[dict]:
    """Expand a {teacher?, student?, stimulus?} value.

    Student pages: student facet, then stimulus — the worksheet reads task-then-surface —
    and nothing else: teacher script never reaches the worksheet, and a null/absent
    student facet renders nothing (so oral/teacher-led tasks leave no trace).

    Teacher pages: stimulus + teacher facet as plain script, then the
    student facet as ONE quoted "Students see" line — the teacher reads their own script and
    the exact prompt students will work from, the way a printed teacher edition shows both.
    Neither facet is a callout: callouts are reserved for the few moments a teacher must not
    miss, and a page where every task is boxed highlights nothing."""
    out: list[dict] = list(_as_blocks(val.get("stimulus")))
    if audience != "teacher":
        out[:0] = _as_blocks(val.get("student"))
        return out
    t_blocks = _as_blocks(val.get("teacher"))
    if len(t_blocks) == 1 and t_blocks[0].get("type") == "list":
        # A list-form script renders as a real list — one glanceable move per line —
        # not a paragraph with dash-prefixed lines.
        out.append(t_blocks[0])
    else:
        t = _facet_text(val.get("teacher"))
        if t:
            out.append({"type": "instructions", "text": t})
        else:
            out.extend(t_blocks)
    s = _facet_text(val.get("student"))
    if s:
        out.append({"type": "labeled", "label": "Students see", "text": s})
    else:
        out.extend(_as_blocks(val.get("student")))
    return out


def expand_from_shared(key: str, shared: dict, audience: str = "teacher",
                       blk: dict | None = None) -> list[dict]:
    """Expand a `{"type": "from_shared", "key": ...}` block into plain renderer blocks.

    The registry is freeform: any key the model registered in `shared` resolves the same way.
    The only special case is `standard`, which is stored under `standard_code`/`standard_text`
    rather than a single key.

    audience: "teacher" (lesson plan / observation) or "student" (worksheet).
    blk: the originating from_shared block — carries an optional `label` for numbered tasks.
    """
    shared = dict(shared or {})
    if key == "standard":
        if not (shared.get("standard_text") or shared.get("standard_code")):
            return []
        return [{"type": "callout", "kind": "special",
                 "label": f"{shared.get('standard_code', '')} — Target standard".strip(" —"),
                 "text": shared.get("standard_text", "")}]

    val = shared.get(key)
    if val is None or val == "" or val == []:
        return []
    if key in _IDENTITY_KEYS:
        return [{"type": "paragraph", "text": str(val)}]

    if isinstance(val, dict) and not _is_block(val) and (
            "teacher" in val or "student" in val or "stimulus" in val):
        out = _faceted(val, audience)
    else:
        out = _as_blocks(val)

    # `{type: from_shared, key: p1, label: "1"}` — fold the label into the first text-bearing
    # block (scanning past leading diagram blocks, which have nothing to fold into) so a
    # numbered prompt renders on one line, not an orphan number above a paragraph.
    # A label must never render alone. Dispatch on that block's FIELDS, not its
    # type name — type names change (callout -> instructions broke the old version of
    # this); the text/label/items field shapes are the schema's stable contract.
    label = (blk or {}).get("label")
    if label and out:
        i = next((j for j, b in enumerate(out)
                  if b.get("label") or b.get("text") or b.get("items")), 0)
        first = out[i]
        if first.get("label"):
            out[i] = {**first, "label": f"{label}. {first['label']}"}
        elif first.get("text"):
            out[i] = {"type": "labeled", "label": str(label), "text": first["text"]}
        elif first.get("items"):
            items = list(first["items"])
            out[i] = {"type": "labeled", "label": str(label), "text": str(items[0])}
            if items[1:]:
                out.insert(i + 1, {**first, "items": items[1:]})
        else:
            out.insert(i, {"type": "labeled", "label": str(label), "text": ""})
    return out


def expand_blocks(blocks: list, shared: dict, audience: str = "teacher") -> list[dict]:
    """Replace any from_shared blocks in a block list (recursing into columns and groups)."""
    out: list[dict] = []
    for blk in blocks or []:
        btype = blk.get("type")
        if btype == "from_shared":
            out.extend(expand_from_shared(blk.get("key", ""), shared, audience, blk))
        elif btype == "columns":
            out.append({"type": "columns",
                        "left": expand_blocks(blk.get("left", []), shared, audience),
                        "right": expand_blocks(blk.get("right", []), shared, audience)})
        elif btype == "group":
            out.append({**blk, "blocks": expand_blocks(blk.get("blocks", []), shared, audience)})
        else:
            out.append(blk)
    return out


_PROMPT_TYPES = ("paragraph", "labeled", "callout", "list", "h3")


def _pair_writing_space(blocks: list[dict]) -> list[dict]:
    """Glue a prompt block to the workspace/answer_box that follows it so a page break can
    never separate a question from its writing space (renderers keep groups together).
    Types are compared post-alias (btype) so canonical and legacy names both pair."""
    out: list[dict] = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if (btype(b) in _PROMPT_TYPES and i + 1 < len(blocks)
                and btype(blocks[i + 1]) == "workspace"):
            out.append({"type": "group", "blocks": [b, blocks[i + 1]]})
            i += 2
            continue
        out.append(b)
        i += 1
    return out


def _strip_heading_echo(section: dict) -> dict:
    """Drop a leading repeat of the section heading from the first text block —
    'If you finish early' + text starting 'If you finish early: …' prints twice."""
    heading = str(section.get("heading", "")).strip().rstrip(":").strip()
    blocks = section.get("blocks") or []
    if not heading or len(heading) < 4 or not blocks:
        return section
    first = blocks[0]
    btype = first.get("type")
    target = first if btype in ("paragraph", "labeled", "callout") else None
    if btype == "group" and first.get("blocks"):
        inner = first["blocks"][0]
        target = inner if inner.get("type") in ("paragraph", "labeled", "callout") else None
    if not target or not isinstance(target.get("text"), str):
        return section
    m = re.match(r"\s*\**" + re.escape(heading) + r"\**\s*[:!.—–-]\s*", target["text"],
                 re.IGNORECASE)
    if not m or not target["text"][m.end():].strip():
        return section
    fixed = dict(target, text=target["text"][m.end():])
    if btype == "group":
        new_first = dict(first, blocks=[fixed] + first["blocks"][1:])
    else:
        new_first = fixed
    return {**section, "blocks": [new_first] + blocks[1:]}


def expand_document(data: dict, audience: str = "teacher") -> dict:
    """Return a copy of a document dict with all from_shared blocks expanded."""
    shared = data.get("shared", {})
    doc = dict(data)
    doc["sections"] = [
        {**s, "blocks": expand_blocks(s.get("blocks", []), shared, audience)}
        for s in data.get("sections", [])
    ]
    # Print-safety repair pass — post-expansion so it covers model prose AND shared content,
    # in every artifact and both output formats (HTML and docx render through here).
    doc["sections"] = [
        {**s, "blocks": _pair_writing_space(
            [rb for b in s.get("blocks", [])
             for eb in _repair_enum_breaks(b)
             for tb in _repair_pipe_tables(eb)
             for rb in _repair_inline_bullets(tb)])}
        for s in doc["sections"]
    ]
    doc["sections"] = [_strip_heading_echo(s) for s in doc["sections"]]
    text = _doc_text(doc["sections"])
    if UNKNOWN_SYMBOL in text and not _UNKNOWN_DEFINED.search(text):
        for s in doc["sections"]:
            if UNKNOWN_SYMBOL in _doc_text([s]):
                s.setdefault("blocks", []).append(
                    {"type": "paragraph",
                     "text": "*The symbol ■ stands for the unknown number.*"})
                break
    return doc


# ============================================================================
# Shared rendering primitives — format-agnostic helpers used by every renderer.
# Moved from render_lesson_html.py so render_lesson_docx.py can import the same
# theme, alias, callout, and grade-band logic without duplication.
# ============================================================================

DEFAULT_THEME = {
    "primary": "#17A267", "title_color": "#14613F",
    "text": "#222222", "muted": "#666666", "rule": "#D0D4D8", "border": "#CBD2D8",
    "title_size": 22, "body_size": 10.5,
}
HEX = re.compile(r"^#[0-9A-Fa-f]{3,8}$")

# Legacy block-type names -> canonical names. Keeps existing lesson JSONs rendering.
ALIASES = {"subheading": "h3", "bullets": "list", "answer_box": "workspace",
           "data_table": "table",
           # frame_bank retired as a component: legacy JSON renders as a plain
           # labeled list — sentence supports are ordinary text the model
           # composes, not a boxed special.
           "frame_bank": "list"}


def btype(blk: dict) -> str:
    t = blk.get("type") or "paragraph"
    return ALIASES.get(t, t)


# Callout kinds: semantic name -> (icon, css class). Legacy `style`/`role` values map in.
CALLOUT_KINDS = {
    "special":      ("⭐", "special"),
    "student-task": ("📌", "task"),
    "teacher-note": ("✋", "tnote"),
    "student-note": ("✋", "snote"),
}
CALLOUT_ALIASES = {
    "accent": "special", "standard": "special",
    "info": "student-task", "activity": "student-task",
    "note": "teacher-note", "tip": "teacher-note",
    "warning": "teacher-note", "caution": "teacher-note", "important": "special",
}


def resolve_callout_kind(blk: dict) -> str:
    raw = str(blk.get("kind") or blk.get("role") or blk.get("style") or "student-task").lower()
    return raw if raw in CALLOUT_KINDS else CALLOUT_ALIASES.get(raw, "student-task")


class Theme:
    def __init__(self, overrides: dict | None):
        t = dict(DEFAULT_THEME)
        t.update(overrides or {})
        self.raw = t
        self.answer_height, self.answer_gap, self.answer_row = 120.0, 22.0, 96.0
        self.ruled_default = False
        self.student_doc = False

    def safe(self, key: str) -> str:
        val = str(self.raw.get(key, DEFAULT_THEME.get(key, "")))
        return val if HEX.match(val) else str(DEFAULT_THEME.get(key, "#222222"))


def meta_text(meta) -> str:
    """Normalize `meta` to a display string. The schema says it's a string, but models
    sometimes emit a list of {label, value} dicts — join those as 'Label: value · …'."""
    if isinstance(meta, dict):
        meta = [meta]
    if isinstance(meta, (list, tuple)):
        parts = []
        for item in meta:
            if isinstance(item, dict):
                label = str(item.get("label") or "").rstrip(":").strip()
                value = str(item.get("value") or item.get("text") or "").strip()
                parts.append(f"{label}: {value}" if label and value else (value or label))
            elif item:
                parts.append(str(item))
        return " · ".join(p for p in parts if p)
    return str(meta) if meta else ""


def grade_number(data: dict):
    """Best-effort grade parse: 0 for K, 1-12, or None."""
    shared = data.get("shared") or {}
    for src in (data.get("grade"), shared.get("grade") if isinstance(shared, dict) else None):
        s = str(src or "").strip().lower()
        if not s:
            continue
        if s.startswith("k") or "kind" in s:
            return 0
        m = re.search(r"\d{1,2}", s)
        if m:
            return int(m.group(0))
    for which, src in (("eyebrow", data.get("eyebrow")), ("meta", meta_text(data.get("meta")))):
        s = str(src or "").lower()
        if "kindergarten" in s:
            return 0
        m = (re.search(r"\bgrade[:\s]*(k|\d{1,2})\b", s)
             or re.search(r"\b(\d{1,2})(?:st|nd|rd|th)[\s-]*grade\b", s))
        if not m and which == "eyebrow":
            m = re.search(r"^\s*(k|1[0-2]|[1-9])(?:st|nd|rd|th)?\b"
                          r"(?!\s*(?:min|minute|hour|problem|tier|page|point|task|question))", s)
        if m:
            g = m.group(1)
            return 0 if g == "k" else int(g)
    return None


def answer_profile(data: dict) -> tuple:
    """Grade-banded writing-space defaults:
    (height pt, ruled line gap pt, table-row pt, ruled by default).

    Math work space is open by default; a block's explicit `ruled: true`
    still gets the band's gap, so a grade-1 sentence answer gets K-2 pitch."""
    n = grade_number(data)
    if n is None:
        return 120.0, 22.0, 96.0, False
    shared = data.get("shared")
    shared = shared if isinstance(shared, dict) else {}
    # smps (Standards for Mathematical Practice) is the most reliable math signal — it is
    # math-only and the math reference mandates it, whereas shared.subject is often omitted.
    is_math = bool(shared.get("smps")) or "math" in " ".join(str(x or "") for x in (
        shared.get("subject"), data.get("eyebrow"), data.get("title"))).lower()
    if n <= 2:
        return 200.0, 40.0, 160.0, not is_math
    if n <= 5:
        return 150.0, 28.0, 126.0, not is_math
    if n <= 8:
        return 130.0, 24.0, 108.0, False
    return 116.0, 22.0, 96.0, False


def coerce_marks(raw):
    """Number-line marks: bare numbers or {position/value, label} dicts -> [(value, label)].
    Models write both forms; a mark the renderer can't read must never vanish silently —
    a task that says "the point for 1/6 is shown" depends on it being drawn."""
    out = []
    for m in raw or []:
        if isinstance(m, (int, float)) and not isinstance(m, bool):
            out.append((float(m), None))
        elif isinstance(m, dict):
            v = m.get("position", m.get("value", m.get("x")))
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                lab = m.get("label")
                out.append((float(v), str(lab) if lab not in (None, "") else None))
    return out


WORKSPACE_SIZES = {"small": 70.0, "med": 130.0, "large": 220.0}
FILL_IN_CHARS = {"short": 12, "med": 28, "long": 60}  # underscore counts for non-CSS formats


def workspace_height(blk: dict, theme: Theme) -> float:
    """Resolve a workspace block's height in points (format-agnostic)."""
    h = blk.get("height_pt")
    if h is None:
        h = WORKSPACE_SIZES.get(str(blk.get("size", "")).lower())
    if h is None:
        h = theme.answer_height
    try:
        return float(h)
    except (TypeError, ValueError):
        return float(theme.answer_height)


def label_text(blk: dict) -> str:
    """Normalized label string — strips a trailing colon so renderers can add their own
    consistently without doubling it."""
    return str(blk.get("label", "")).rstrip(":")


def label_sep(label: str) -> str:
    """Separator after a label: numeric labels (task numbers like "1", "2a") get a period;
    word labels ("Anchor task", "Exit ticket") get a colon. A label that already ends in a
    period gets no extra separator."""
    s = label.strip()
    if s.endswith("."):
        return ""
    return "." if re.fullmatch(r"\d+[a-z]?", s, re.IGNORECASE) else ":"


def normalize_text(text) -> str:
    """Format-agnostic text fixups applied before any inline-markdown parse."""
    t = str(text)
    t = re.sub(r"(?<!_)_{3,9}(?!_)", "______", t)
    t = re.sub(r"\s+\|\s+", " · ", t)
    return t


_MD_TOKEN = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*(?!\s).+?(?<!\s)\*(?!\*)|\n)")


def md_tokens(text) -> list:
    """Parse mini-markdown into format-neutral tokens.

    Returns a list of (text, attrs) where attrs is a dict with optional 'bold',
    'italic', 'break' keys. normalize_text() is applied first."""
    t = normalize_text(text)
    out = []
    for part in _MD_TOKEN.split(t):
        if not part:
            continue
        if part == "\n":
            out.append(("", {"break": True}))
        elif part.startswith("**") and part.endswith("**"):
            out.append((part[2:-2], {"bold": True}))
        elif part.startswith("*") and part.endswith("*"):
            out.append((part[1:-1], {"italic": True}))
        else:
            out.append((part, {}))
    return out


def coerce_rows(rows) -> list[list]:
    """Normalize model-emitted table rows. Each row must be a list of cells, but models
    sometimes emit a bare string ("Total: $5.99"), a dict ({"label": ..., "value": ...}),
    or null — coerce instead of crashing (docx KeyError) or garbling (one cell per
    character); null becomes a blank write-in row."""
    if isinstance(rows, str):
        # The whole rows value drawn as one pipe string — restore rows and cells.
        rows = _parse_pipe_rows(rows.splitlines()) if "|" in rows else [[rows]]
    out: list[list] = []
    for r in rows or []:
        if isinstance(r, list):
            out.append(r)
        elif isinstance(r, dict):
            out.append(list(r.values()))
        elif r is None:
            out.append([])
        else:
            out.append([str(r)])
    return out


def coerce_headers(headers) -> list:
    """Normalize table headers. A bare string ("Item | Cost") is the pipe-joined header
    row a model meant — split it; a dict's values are its labels; any other non-list
    becomes a single header."""
    if isinstance(headers, list):
        return headers
    if not headers:
        return []
    if isinstance(headers, dict):
        return list(headers.values())
    s = str(headers)
    if "|" in s:
        parsed = _parse_pipe_rows([s])
        return parsed[0] if parsed else []
    return [s]


def table_row_height(blk: dict, theme: Theme, *, full_blank: bool) -> float:
    """Minimum height (pt) for a table row containing empty writing-space cells.
    An explicit empty_row_height_pt / row_height_pt wins (floored at the 40pt
    writable minimum the deterministic checks enforce) — a sort grid whose cells
    take an X is deliberately shorter than a sentence row, and flooring it to
    the grade band printed near-blank pages of grid. The band sizes rows only
    when the model didn't say."""
    try:
        explicit = float(blk.get("empty_row_height_pt")
                         or blk.get("row_height_pt") or 0)
    except (TypeError, ValueError):
        explicit = 0.0
    band = theme.answer_row
    if theme.student_doc:
        if explicit:
            return max(explicit, 40.0)
        return band if full_blank else 0.45 * band
    return explicit or 36.0


def preamble_blocks(data: dict) -> list[dict]:
    """Top-level standard / prerequisite / practices blocks rendered between the header
    and the first section. Shared by both formats so the preamble can never drift."""
    blocks: list[dict] = []
    if data.get("standard_text"):
        label = f"{data.get('standard_code', '')} — Target standard".strip(" —")
        blocks.append({"type": "callout", "kind": "special", "label": label,
                       "text": data["standard_text"]})
    if data.get("prerequisite_standard"):
        blocks.append({"type": "labeled", "label": "Builds on",
                       "text": data["prerequisite_standard"]})
    if data.get("smps"):
        blocks.append({"type": "labeled", "label": "Mathematical practices",
                       "text": "; ".join(data["smps"])})
    return blocks


def build_header(data: dict) -> dict:
    """Format-agnostic header fields: eyebrow, title, meta string, optional name_line."""
    meta = meta_text(data.get("meta"))
    if not meta:
        bits = [data.get("standard_code"), data.get("grade"), data.get("duration"),
                data.get("curriculum")]
        if data.get("materials"):
            bits.append("Materials: " + ", ".join(data["materials"]))
        meta = " · ".join(str(b) for b in bits if b)
    name_line = ""
    if meta and data.get("audience") == "student" and re.search(r"name\s*:", meta, re.I):
        name_line, meta = meta, ""
    return {"eyebrow": data.get("eyebrow", ""), "title": data.get("title", "Lesson Plan"),
            "meta": meta, "name_line": name_line}
