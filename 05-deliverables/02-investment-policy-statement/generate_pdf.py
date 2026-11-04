"""Export the unchanged submitted IPS as a formatted archival PDF.

Run with .context/ips-pdf-venv/bin/python (reportlab and pypdf installed).
Official title fields were verified from the submitted roster on 4 Nov 2026.
This generates a local copy; it does not modify the online submission.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import json
import re

from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer,
)
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('submitted.md')
OUTPUT = ROOT / 'output/pdf/Komodos_Investment_Policy_Statement.pdf'
CHECKS = ROOT / '.context/ips-pdf-validation.json'
FONT_DIR = Path('/System/Library/Fonts/Supplemental')


def norm(value):
    return ' '.join(value.split())


def main():
    source = SOURCE.read_text()
    pitch, statement = source.removeprefix(
        '# Investment Strategy Elevator Pitch\n'
    ).split('# Investment Policy Statement\n')
    pitch, statement = pitch.strip(), statement.strip()
    assert len(pitch.split()) == 46
    assert len(statement.split()) == 498

    pdfmetrics.registerFont(TTFont('TNR', str(FONT_DIR / 'Times New Roman.ttf')))
    pdfmetrics.registerFont(TTFont('TNR-Bold', str(FONT_DIR / 'Times New Roman Bold.ttf')))
    pdfmetrics.registerFontFamily('TNR', normal='TNR', bold='TNR-Bold')

    body = ParagraphStyle('Body', fontName='TNR', fontSize=12, leading=24,
                          alignment=TA_LEFT, spaceAfter=6,
                          allowWidows=0, allowOrphans=0)
    heading = ParagraphStyle('Heading', parent=body, fontName='TNR-Bold',
                             spaceAfter=6, keepWithNext=True)
    cover = ParagraphStyle('Cover', parent=body, alignment=TA_CENTER, spaceAfter=0)
    cover_bold = ParagraphStyle('CoverBold', parent=cover, fontName='TNR-Bold')

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(OUTPUT), pagesize=letter,
                          leftMargin=72, rightMargin=72, topMargin=72, bottomMargin=72,
                          title='Komodos - Investment Policy Statement',
                          author='Komodos', subject='IPS submitted 4 November 2026')
    doc.addPageTemplates(PageTemplate(
        id='IPS', frames=[Frame(72, 72, 468, 648,
                               leftPadding=0, rightPadding=0,
                               topPadding=0, bottomPadding=0)]))

    story = [Spacer(1, 108), Paragraph('Komodos', cover_bold), Spacer(1, 12),
             Paragraph('Investment Policy Statement', cover_bold), Spacer(1, 24)]
    # First-name / last-initial form, preserving the roster's given-name field.
    for name in ['Théodore (Teddy) L.', 'Sebastian M.', 'Nathanael S.',
                 'Lucas M.', 'Marc C.']:
        story.append(Paragraph(escape(name), cover))
    story += [Spacer(1, 24), Paragraph('WInS username: Komodos-10427064', cover),
              PageBreak(), Paragraph('Investment Strategy Elevator Pitch', heading),
              Paragraph(escape(pitch), body), Spacer(1, 6),
              Paragraph('Investment Policy Statement', heading)]
    for paragraph in re.split(r'\n\s*\n', statement):
        story.append(Paragraph(escape(paragraph), body))
    doc.build(story)

    reader = PdfReader(OUTPUT)
    assert len(reader.pages) == 3, f'Expected title + two content pages; got {len(reader.pages)}'
    assert OUTPUT.stat().st_size <= 5_000_000
    extracted = '\n'.join(page.extract_text() for page in reader.pages[1:])
    extracted = extracted.replace('Investment Strategy Elevator Pitch', '', 1)
    extracted = extracted.replace('Investment Policy Statement', '', 1)
    assert norm(extracted) == norm(pitch + '\n' + statement), 'PDF text differs from submitted IPS'
    runs = []
    for page in reader.pages:
        def visitor(text, cm, tm, font, size):
            if text.strip():
                runs.append({'font': str(font.get('/BaseFont', '')), 'size': size})
        page.extract_text(visitor_text=visitor)
    assert all(run['size'] == 12 for run in runs)
    assert all('TimesNewRoman' in run['font'] for run in runs)
    checks = {'pages': len(reader.pages), 'bytes': OUTPUT.stat().st_size,
              'pitch_words': 46, 'statement_words': 498,
              'submitted_text_matches': True, 'font': 'Times New Roman',
              'font_points': 12, 'leading_points': 24, 'margins_points': 72,
              'page_size': 'US Letter', 'output': str(OUTPUT)}
    CHECKS.write_text(json.dumps(checks, indent=2) + '\n')
    print(json.dumps(checks, indent=2))


if __name__ == '__main__':
    main()
