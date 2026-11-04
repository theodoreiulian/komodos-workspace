"""Count the two IPS submission fields; do not include headings or review notes.

Whitespace counting is the ordinary count. The conservative check also splits
hyphenated words and words separated by dashes. This is a reproducible house
check, not a claim about the submission form's tokenizer.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DRAFT = ROOT / '05-deliverables/02-investment-policy-statement/draft.md'
OUTPUT = ROOT / '03-modeling/output/ips_word_counts_2026_11_04.json'


def main():
    draft = DRAFT.read_text()
    pitch_heading = '# Investment Strategy Elevator Pitch\n'
    statement_heading = '# Investment Policy Statement\n'
    assert draft.count(pitch_heading) == 1
    assert draft.count(statement_heading) == 1
    pitch, statement = draft.removeprefix(pitch_heading).split(statement_heading)
    result = {}
    for name, body, limit in [('pitch', pitch.strip(), 50),
                              ('statement', statement.strip(), 500)]:
        ordinary = len(body.split())
        conservative = len(re.sub(r'[-\u2010-\u2015]', ' ', body).split())
        assert ordinary <= limit and conservative <= limit, (name, ordinary, conservative)
        assert not re.search(r'https?://|!\[|\]\(|\[\^', body), name
        result[name] = {'words': ordinary, 'conservative_words': conservative,
                        'limit': limit, 'within_limit': True}
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
