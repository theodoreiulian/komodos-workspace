# The Komodos — Wharton Global High School Investment Competition 2026–27

Team workspace for **The Komodos**, American Section, Lycée International de
Saint-Germain-en-Laye, France. Four students + teacher advisor.

**Client:** Laura Gao — author, illustrator, entrepreneur (Wharton W'18).
**The job:** design, implement, articulate and evaluate a long-term investment
strategy that funds a ten-year, $500,000 operating commitment for a creative
residency in Taiwan with a high degree of certainty, and tells Laura how much
she can responsibly promise co-sponsors toward the facility itself.

---

## The one thing to remember

> This is **not** a stock-picking contest. Gains and losses in the simulator do
> not select winners. The competition rewards a *cohesive strategy* — one clear
> idea, carried consistently through research, trades, the IPS and the Final
> Report. Judges want the **reasoning, assumptions and tradeoffs**.

---

## Calendar (all deadlines 5:00 p.m. ET — no extensions, ever)

| Date | What |
|---|---|
| Sep 15 – Sep 25, 2026 | WInS practice period (account wiped afterwards) |
| **Sep 28, 2026** | Official trading begins |
| **Oct 9, 2026** | Official Team Roster due — *roster locks* |
| **Oct 23, 2026** | Trading Notes Analysis due |
| **Nov 6, 2026** | Investment Policy Statement due — *strategy locks, portfolio freezes* |
| Nov 9, 2026 | Final Report requirements published |
| **Dec 4, 2026** | Final Report + official school documentation due |
| Spring 2027 | Top-50 semifinals (virtual) → Top-10 Global Finale, Philadelphia, Apr 29–30 |

---

## Who does what

| | Does |
|---|---|
| **Claude (lead strategist)** | Research, modelling, and every strategy and trade decision. Logs each decision and writes a plain-language brief so the team can explain and defend it. Works to `CLAUDE.md` and `99-admin/playbook.md`. |
| **Team Leader** | Kept in the loop through the briefs; explains decisions to the team; can veto any decision. Sole contact with Wharton; submits everything; roster and school letter. |
| **The whole team** | Enters trades and Trading Notes in WInS exactly as specified; writes every submitted word in their own voice; presents at semifinals and the finale. |

---

## How this repo is laid out

```
CLAUDE.md         Claude's charter: role, session routine, rules, the integrity line.
.claude/agents/   The subagents Claude uses (researcher, quant-modeler, red-team,
                  judge-panel, rules-auditor, beginner-reader).
00-competition/   The rules of the game. Authoritative.
                  └ source-documents/   Original PDFs, archived.
01-research/      Everything learned so far: knowledge base, market context, past
                  winners, candidate strategic angles.
02-strategy/      The strategy in force. Empty until Claude decides the thesis.
03-modeling/      Python models, simulations, outputs. Reproducible numbers only.
04-portfolio/     Trade instructions, trade log, Trading Notes as entered in WInS.
05-deliverables/  The three graded submissions, written by the students.
06-team/briefings/  Claude's plain-language briefs to the Team Leader, one per decision.
99-admin/         state.md (where things stand, what's next), decision-log.md,
                  playbook.md (how Claude works), ai-use-log.md (disclosure record).
```

**Start here:** `99-admin/state.md` for what is happening now, then the latest
brief in `06-team/briefings/`.

---

## Working rules

1. **Every number is reproducible.** If a figure appears in a deliverable it
   comes from a script in `03-modeling/` or a cited source.
2. **The Trading Note is written before the trade**, and entered in WInS word
   for word as specified. Wharton checks notes against executed trades.
3. **Every decision is logged** in `99-admin/decision-log.md` the day it is
   made, including reversals.
4. **The AI policy is followed to the letter.** Claude decides and analyses, but
   writes no submitted prose. Everything Claude contributes is recorded in
   `99-admin/ai-use-log.md` and disclosed in the Final Report's Works Cited.
5. **Start from the client, end at the client.** Anything that could have been
   written about a generic investor is wasted.
