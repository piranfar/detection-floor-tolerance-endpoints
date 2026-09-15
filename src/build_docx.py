"""
The article and the supplement as two Word files, for reading and marking up.

Run:  python -m src.build_docx

WHY. The submission folder carried Markdown, and Markdown is the right format for
a file that a program builds and an audit reads. It is the wrong format for the
one thing a manuscript has to survive: somebody opening it, disagreeing with a
sentence, and writing in the margin. That happens in Word, so the same two
documents are emitted here as .docx -- the article and the supplement SEPARATELY,
because the journal takes them as separate uploads and a reviewer reads them as
separate documents.

WHAT IS NOT DONE HERE. Nothing is authored, reworded or reordered. This is a
renderer: it reads manuscript/SUBMISSION_MAIN.md and SUBMISSION_SUPPLEMENT.md,
which src.build_submission wrote, and lays them out. If a sentence is wrong in
the .docx it is wrong in the Markdown, and the Markdown is where it gets fixed.

Figures are placed ABOVE their legends rather than collected at the end, because
a legend without its figure is unreadable and the point of this file is that it
be read. The image is the 600 dpi PNG the figure scripts already wrote.

Set double spacing and continuous line numbers, which is what a manuscript under
review is marked up on: "page 7, line 231" is a usable reference and "the third
paragraph of the Discussion" is not.

Writes:
  submission/02_manuscript.docx
  submission/03_supplementary_material.docx
"""
from __future__ import annotations

import re
from pathlib import Path
from .figure_manifest import image_map

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript" / "SUBMISSION_MAIN.md"
SUPP = ROOT / "manuscript" / "SUBMISSION_SUPPLEMENT.md"
FIGDIR = ROOT / "results" / "figures"
OUT = ROOT / "submission"

# Which image belongs to which legend. The legends say "Figure 2"; the scripts
# that drew them are named for what they compute, and nothing in either name
# tells you about the other, so the mapping is written down once here.
FIGURE_IMAGE = image_map()

LEGEND = re.compile(r"^\*\*Figure (S?\d+)\.")
TABLE_ROW = re.compile(r"^\s*\|")
TABLE_RULE = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
# **bold** and *italic*, taken in that order so the two asterisks win.
INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*\n]+?\*)")


def add_line_numbers(doc: Document) -> None:
    """Continuous line numbers down the left margin."""
    sect = doc.sections[0]._sectPr
    ln = OxmlElement("w:lnNumType")
    ln.set(qn("w:countBy"), "1")
    ln.set(qn("w:restart"), "continuous")
    ln.set(qn("w:distance"), "360")
    sect.append(ln)


def add_page_numbers(doc: Document) -> None:
    """A PAGE field in the footer, centred."""
    for section in doc.sections:
        p = section.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        for instr, kind in (("begin", "w:fldCharType"),):
            el = OxmlElement("w:fldChar")
            el.set(qn(kind), instr)
            run._r.append(el)
        instr = OxmlElement("w:instrText")
        instr.set(qn("xml:space"), "preserve")
        instr.text = "PAGE"
        run._r.append(instr)
        end = OxmlElement("w:fldChar")
        end.set(qn("w:fldCharType"), "end")
        run._r.append(end)


def style_document(doc: Document, double_spaced: bool) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    pf = normal.paragraph_format
    pf.line_spacing = 2.0 if double_spaced else 1.15
    pf.space_after = Pt(0 if double_spaced else 6)
    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(1)
        section.top_margin = section.bottom_margin = Inches(1)


def write_runs(par, text: str) -> None:
    """Render **bold** and *italic* as runs; everything else is plain."""
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            par.add_run(piece[2:-2]).bold = True
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            par.add_run(piece[1:-1]).italic = True
        else:
            par.add_run(piece)


def add_table(doc: Document, rows: list[str]) -> None:
    """A Markdown pipe table as a real Word table."""
    grid = []
    for line in rows:
        if TABLE_RULE.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        grid.append(cells)
    if not grid:
        return
    width = max(len(r) for r in grid)
    table = doc.add_table(rows=0, cols=width)
    table.style = "Table Grid"
    table.autofit = True
    for i, cells in enumerate(grid):
        cells = cells + [""] * (width - len(cells))
        row = table.add_row().cells
        for cell, text in zip(row, cells):
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.line_spacing = 1.0
            par.paragraph_format.space_after = Pt(2)
            write_runs(par, text)
            for run in par.runs:
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True
    doc.add_paragraph()


def add_figure(doc: Document, number: str) -> bool:
    stem = FIGURE_IMAGE.get(number)
    if not stem:
        return False
    img = FIGDIR / f"{stem}.png"
    if not img.exists():
        return False
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.line_spacing = 1.0
    par.add_run().add_picture(str(img), width=Inches(6.0))
    return True


def render(md: str, title_hint: str, double_spaced: bool) -> Document:
    doc = Document()
    style_document(doc, double_spaced)
    add_line_numbers(doc)
    add_page_numbers(doc)

    # Drop the YAML front matter; its title is repeated as the `# ` heading.
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    lines = md.split("\n")

    i, buf = 0, []

    def flush() -> None:
        """Emit whatever plain text has accumulated as one paragraph."""
        nonlocal buf
        if not buf:
            return
        text = " ".join(x.strip() for x in buf).strip()
        buf = []
        if not text:
            return
        m = LEGEND.match(text)
        if m:
            add_figure(doc, m.group(1))
            par = doc.add_paragraph()
            par.paragraph_format.line_spacing = 1.15
            par.paragraph_format.space_after = Pt(12)
            write_runs(par, text)
            for run in par.runs:
                run.font.size = Pt(10)
            return
        write_runs(doc.add_paragraph(), text)

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if TABLE_ROW.match(line):
            flush()
            rows = []
            while i < len(lines) and TABLE_ROW.match(lines[i]):
                rows.append(lines[i])
                i += 1
            add_table(doc, rows)
            continue

        if not stripped:
            flush()
            i += 1
            continue

        if stripped.startswith("#"):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            if level == 1:
                par = doc.add_paragraph()
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                write_runs(par, text)
                for run in par.runs:
                    run.bold = True
                    run.font.size = Pt(14)
            else:
                par = doc.add_paragraph()
                par.paragraph_format.space_before = Pt(12)
                write_runs(par, text)
                for run in par.runs:
                    run.bold = True
                    run.font.size = Pt(12 if level == 2 else 11)
            i += 1
            continue

        if stripped in ("---", "***", "___"):
            flush()
            i += 1
            continue

        # An indented block is the one display equation this paper has.
        if line.startswith("    ") and stripped:
            flush()
            par = doc.add_paragraph()
            par.paragraph_format.left_indent = Inches(0.5)
            par.paragraph_format.line_spacing = 1.0
            run = par.add_run(stripped)
            run.font.name = "Consolas"
            run.font.size = Pt(11)
            i += 1
            continue

        buf.append(line)
        i += 1

    flush()
    return doc


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [
        (MAIN, OUT / "02_manuscript.docx", "article", True),
        (SUPP, OUT / "03_supplementary_material.docx", "supplement", False),
    ]
    missing = [p.name for p, _, _, _ in jobs if not p.exists()]
    if missing:
        raise SystemExit(f"missing {missing}; run python -m src.build_submission")

    for src, dest, what, double in jobs:
        doc = render(src.read_text(encoding="utf-8"), what, double)
        doc.save(dest)
        words = len(src.read_text(encoding="utf-8").split())
        print(f"   {dest.name:34} {words:>7,} words  "
              f"({'double' if double else 'single'}-spaced, line-numbered)")
    print(f"wrote {OUT.relative_to(ROOT)}/ -- article and supplement as "
          f"separate Word files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
