# Decision log

Every strategic decision, the day it is made, by **Claude (lead strategist)**
unless it says otherwise. Reversals get logged as new entries, never by editing
the old one. Evaluation criterion 4 asks us to explain our decision-making
process and how our thinking changed. A reversal with a reason is better
material than a straight line.

Tiers and the protocol behind each entry: `99-admin/playbook.md` Part 3.

---

### Template
```
## YYYY-MM-DD — <decision in one line>
**Tier:** 2 | 3
**Status:** Decided | Reversed (see <date>) | Vetoed by Team Leader (see <date>)
**Question:** what was being decided, and what depended on it
**Options considered:** A, B, C
**Decision:** what was chosen
**Reasoning:** why, in plain words
**Evidence:** script output, doc or source
**Strongest objection (red team) and the answer:**
**Revisit when:** the specific trigger that would reopen it
**Brief:** 06-team/briefings/<file>
```

---

## 2026-09-29 — Decision authority moves to Claude; all earlier decisions cancelled
**Tier:** 3
**Status:** Decided — by the Team Leader
**Question:** Who drives the strategy?
**Decision:** The Team Leader made Claude the lead strategist and primary
decision-maker, with full autonomy over research, analysis, strategy and trade
decisions. The students keep: entering trades in WInS, writing all submitted
text, presenting, admin, and a veto. Every decision the team had made before
this date is cancelled and reopened:
- Adopting Angle B ("engineer the certainty") as the governing thesis (23 Sep)
- Committing to the Treasury ladder before checking what WInS lists (23 Sep)
- The team working model: no standing roles, weekly task log (23 Sep)

The research behind these decisions is kept. The arguments made for and against
Angle B were moved to `01-research/differentiation-angles.md` as evidence, not
as a verdict. The earlier text is in git history (commit `68ae88e`).
**Reasoning:** The Team Leader's judgement was that decisions based on deeper
research would be better informed than the team's.
**⚠️ Integrity note:** Wharton treats substantial completion of a task by AI
like substantial completion by another person, and requires AI material to be
cited. The safeguards are set out in `CLAUDE.md` ("The integrity line"): Claude
writes no submission prose, every contribution is logged in
`99-admin/ai-use-log.md` for the Works Cited, and each decision is briefed so the
students can defend it themselves.
**Revisit when:** The Team Leader says so.

---

## Open questions

Owned by Claude. Priority order and dates live in `99-admin/state.md`.

| # | Question | What depends on it |
|---|---|---|
| ~~Q1~~ | ✅ **Answered 29 Sep** — full 2033–42 ladder buildable; see `04-portfolio/wins-instruments.md`. Was: What can WInS actually trade? Individual Treasuries 2033–2042? STRIPS (bonds that pay one amount at maturity and nothing before)? Target-maturity bond ETFs (funds that hold bonds maturing in one year, then close and pay out)? | Whether a matched ladder can be built at all |
| Q2 | **The governing thesis.** Structural certainty (a ladder), statistical certainty (a probability from simulations), or a mix? Reopened from scratch. | Everything |
| Q3 | How much to lock in, and when: all of the promise in 2027, part of it, or step by step on a pre-set rule? | Reserve design, how much is left to grow |
| Q4 | What goes in the growth portion, and how much risk does it take? | Trades, Trading Notes, the facility gift |
| Q5 | Does the growth portion reduce risk ahead of 2033, and on what rule? | "Changing time horizons" (criterion 1) |
| Q6 | How is the co-sponsor range built — floor, middle, top, and what confidence level? | Final Report, criterion 5 |
| Q7 | Does Laura's creative income being exposed to AI change a real allocation (Angle A)? If not, drop it. | Whether the thesis is specific to Laura |
| Q8 | Model upgrades: historical resampling of returns instead of the current simplified random returns; interest rates that move; costs and inflation. | Whether the numbers are publishable |
| Q9 | Which 3 Trading Notes go in the 23 Oct analysis? Means the trades behind them must be executed well before then. | Trading Notes Analysis |
