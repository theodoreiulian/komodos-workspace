# Current state — Claude's working file

Read this at the start of every session and update it at the end. It is the
handoff between sessions.

**Last updated:** 2026-09-29 (repo restructured; Claude takes over as lead strategist)

---

## Where things stand

- **Official trading opened 28 Sep.** Nothing has been traded. The window closes
  6 Nov.
- **No strategy decisions are in force.** All earlier team decisions were
  cancelled on 29 Sep. The research base is intact: `01-research/`,
  `03-modeling/`.
- **The WInS practice window (15–25 Sep) has closed.** We don't know whether
  anyone checked which instruments WInS lists (Q1). This is now the most urgent
  unknown — it decides whether a matched Treasury ladder can be built at all.
- Existing model numbers use simplified random returns (i.i.d. lognormal — each
  year drawn independently from one bell-shaped curve) and the 15 Sep 2026 yield
  curve. Good enough to choose a direction, **not good enough to publish**.

## Critical path

Deadlines are 5:00 p.m. ET = 11:00 p.m. in France. Aim to finish 24 hours early.

| By | What | Why then |
|---|---|---|
| **1 Oct** | Q1 answered: exact list of the relevant WInS instruments. Treasury curve refreshed to the latest date. | Everything structural depends on it |
| **6 Oct** | **Q2 + Q3 decided** (thesis and how much to lock in), full Tier 3 protocol. Brief to the Team Leader. | Trades have to start in the first half of October |
| **9 Oct** | First trades specified (exact orders + exact Trading Note text) and entered by the humans. **Roster due** (humans). | Trades for the 23 Oct analysis must already exist, with notes, before we pick three |
| **16 Oct** | Q4, Q5, Q7 decided; remaining core trades placed. Q9: shortlist of Trading Notes and reflection outlines to the students. | Students need a week to write the reflections |
| **23 Oct** | **Trading Notes Analysis due** (students submit) | — |
| **27 Oct** | IPS decision framework final; outline to the students; `judge-panel` + `rules-auditor` pass | Students need ~10 days to write 550 words well |
| **6 Nov** | **IPS due. Strategy and portfolio freeze.** All trading done. | One-way door |
| 9 Nov | Final Report requirements published — read them the same day | — |
| 4 Dec | **Final Report + school letter due** | — |

## Next three things I will do

1. ✅ Q1 answered 29 Sep. Next: re-check iBonds bid/ask during US market hours.
2. Refresh the Treasury curve and re-price the ladder at today's yields
   (`quant-modeler`).
3. Start the Q2 Tier 3 protocol: reopen the thesis from scratch — structural vs
   statistical vs mixed — with two independent `red-team` passes (one arguing "too
   cautious", one arguing "too risky").

## Waiting on the humans

*Done: H3 — Team Leader confirmed aged 17 on 28 Sep 2026 (29 Sep). H2 — roster submitted (29 Sep).*
*Done: H1/Q1 — Claude checked WInS directly (29 Sep). Full ladder 2033–2042 is buildable: iBonds IBTM/IBTO/IBTP/IBTQ for the 2033–36 payments, T-BONDs for 2037–42. See `04-portfolio/wins-instruments.md`. Claude has browser access to the StockTrak account via Claude in Chrome (read-only use unless a trade is agreed).*
*Known: WInS is StockTrak (app.stocktrak.com); account Komodos-10427064; 0/200 trades as of 29 Sep.*

| # | What | Who | Needed by |
|---|---|---|---|
| H4 | School letter — see `06-team/punchlist.md` P1 | Team Leader | ask 30 Sep |

## Coverage of the five judging criteria

Check weekly. A criterion nobody has worked on is the priority.

| Criterion | State |
|---|---|
| 1 Investment strategy | No thesis in force. Candidates researched. |
| 2 Client knowledge | Client brief done; Laura-specific angle (A) untested |
| 3 Portfolio analysis | First-pass models exist; upgrades needed (Q8) |
| 4 Competition experience | Decision log restarted; AI-use log started |
| 5 Creativity & presentation | Not started; co-sponsor communication is graded here |
