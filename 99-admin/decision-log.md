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
**Status:** Decided | Reversed (see <date>)
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
decisions. Claude also owns drafting, editing and review of all competition
materials. The humans handle account actions, live presentations and school
administration. Every decision the team had made before this date is cancelled
and reopened:
- Adopting Angle B ("engineer the certainty") as the governing thesis (23 Sep)
- Committing to the Treasury ladder before checking what WInS lists (23 Sep)
- The team working model: no standing roles, weekly task log (23 Sep)

The research behind these decisions is kept. The arguments made for and against
Angle B were moved to `01-research/differentiation-angles.md` as evidence, not
as a verdict. The earlier text is in git history (commit `68ae88e`).
**Reasoning:** The Team Leader's judgement was that decisions based on deeper
research would be better informed than the team's.
**Revisit when:** The evidence shows a different operating model would produce
better decisions or execution.

---

## 2026-09-30 — Lock in all ten payments at the start; grow the rest; lock the co-sponsor promise when it is made
**Tier:** 3
**Status:** Decided
**Question:** How does the portfolio fund the ten $50,000 payments (2033–42) "with
a high degree of certainty", and how much should be locked in, and when? (Q2/Q3)
**Options considered:** S1 lock all ten in 2027; S2 lock 2033–37 in 2027, rest in
2031; S3 lock all in 2031; S4 lock nothing until 2033 (60/40 throughout). All
with the same 2031 promise lock except S4. Growth part tested as 100% stocks and
as 60/40.
**Decision:** S1. A "Promise Portfolio" — cash-flow-matched ladder of WInS
T-bonds (2036–41 maturities) and iShares iBonds Treasury funds (IBTO/IBTP/IBTQ),
sized for $51,000 a year (2% buffer); the 2033 bill is paid by the ladder's
pre-2033 coupons, which are ring-fenced. Everything else forms the "Gift
Portfolio". **Promise-lock principle adopted:** in Jan 2031 the bottom of the
co-sponsor range is moved into 2-year Treasuries. Its size (placeholder 75%) is
Q6. **Falling-rate rule:** the ladder is paid for first (from the 2028
contribution if needed); the Gift Portfolio gets what is left. **WInS:** the
$300k account is the $450k plan at 2/3 scale (~$211.5k ladder, 9 trades; rest in
cash until Q4); the fact that the real plan is 100% bonds during 2027 is stated
openly.
**Reasoning:** On the strictest basis for S1 (real instruments, buy prices,
idle cash at 0%, 2% buffer, charged as the same % friction to every rival), in
the central case S1 funds 100% of payments vs 99.96% / 96.34% / 93.37%, with a
p5 gift of $128,642 vs $77,490 / $12,724 / $0, and a median within ~$2,600 of
the best rival. In the low case S1 also has the highest median. Only if stocks
match their long-run history does S1 cost median gift (~$53k vs S4). Safe
yields (10y 5.26%, 29 Sep) ≈ Vanguard's 2026 10-year equity forecasts (US
3.9–5.9%, non-US 4.9–6.9%), so the reward for risk on promised money is small.
**Evidence:** `03-modeling/src/thesis_decision_2026_09_30.py`,
`03-modeling/output/thesis_decision_2026_09_30_run.txt`,
`04-portfolio/wins-instruments.md`, `02-strategy/proposal-2026-09-30.md`.
**Strongest objection (red team) and the answer:** (1) *Too cautious / model
biased to S1* — v1 costed S1 at the smooth curve and rivals at a flat 5.0% 2033
rate and without the promise lock. Fixed: all charged the same friction, rivals
buy at the forward rate (5.66% in 2031, 5.78% in 2033), all get the lock. S1
still wins on certainty and floor, and ties on the median. (2) *Not as safe as
claimed* — funds were assumed to reinvest at their yield while bonds held cash
at 0%, the ladder was dated today rather than 1 Jan 2027, and there was no
buffer. Fixed: one 0%-cash rule, 2027 date, 2% buffer. (3) *The promise lock
sells after a 2028–30 crash; "0% broken" is true by construction* — accepted.
The lock size and the pre-2031 glidepath are deferred to Q5/Q6 and will be
judged on how often the quotable floor is low (<$100k: 19.0% if all stocks,
7.5% if 60/40), not on "broken".
Judge panel: client knowledge 5/10, the weakest criterion, because the Gift
Portfolio says nothing about Laura yet → Q4 brought forward to 7 Oct.
**Revisit when:** WInS prices put the 2/3-scale ladder above ~$230k; the real
plan's ladder would exceed ~$375k (rates ~1.5 points lower); Q4 shows Laura's
situation calls for enough growth that S2 beats S1 on the gift while staying
~100% funded.
**Brief:** 06-team/briefings/2026-09-30-lock-in-the-promise.md

---

## 2026-10-07 — AI authority covers the entire project, including submitted writing
**Tier:** 2
**Status:** Decided — by the Team Leader
**Question:** What parts of the project may AI own and execute?
**Options considered:** Limit AI to research and analysis; allow AI to draft but
not decide; give AI full authority across research, decisions, drafting, editing
and review.
**Decision:** AI has full authority across the project. It is the primary
decision-maker and may draft, edit and review Trading Notes, the Investment
Policy Statement, the Trading Notes Analysis and the Final Report. Humans remain
responsible for identity-bound account actions and live presentations.
**Reasoning:** The Team Leader explicitly removed all AI-specific operating
restrictions and assigned the AI the complete workflow.
**Evidence:** `AGENTS.md`, `CLAUDE.md`, `README.md`, and the repository-wide
workflow audit completed on 7 Oct 2026.
**Strongest objection and the answer:** The operating model must still preserve
all non-AI competition rules, numerical traceability and review standards. Those
controls remain unchanged.
**Revisit when:** The Team Leader explicitly changes the operating model.

---

## 2026-10-07 — The repository is the exclusive authority for competition rules
**Tier:** Operating instruction
**Status:** Decided — by the Team Leader
**Question:** Which sources may agents use to identify or enforce Wharton
competition rules?
**Decision:** Agents use only competition rules recorded inside this repository.
They may not search for, verify against, cite, rely on, or enforce rules from any
external source. If the repository is silent, ambiguous or inconsistent, the
agent reports the gap and asks for an internal clarification instead of looking
outside.
**Reasoning:** The Team Leader requires a stable, explicit rule set that cannot
be expanded or changed by external pages, search results or model memory.
**Evidence:** `00-competition/RULE-AUTHORITY.md`, `AGENTS.md`, `CLAUDE.md`, and
the mirrored instructions in every project agent definition.
**Revisit when:** The Team Leader explicitly changes the rule-source policy.

---

## Open questions

Owned by Claude. Priority order and dates live in `99-admin/state.md`.

| # | Question | What depends on it |
|---|---|---|
| ~~Q1~~ | ✅ **Answered 29 Sep** — full 2033–42 ladder buildable; see `04-portfolio/wins-instruments.md`. Was: What can WInS actually trade? Individual Treasuries 2033–2042? STRIPS (bonds that pay one amount at maturity and nothing before)? Target-maturity bond ETFs (funds that hold bonds maturing in one year, then close and pay out)? | Whether a matched ladder can be built at all |
| ~~Q2~~ | ✅ **Decided 30 Sep**: structural. Lock all ten payments at the start. | — |
| ~~Q3~~ | ✅ **Decided 30 Sep**: all of it, at the start (1 Jan 2027 in the plan; now in WInS). | — |
| Q4 | What goes in the Gift Portfolio, how much risk, and what makes it Laura's? **Due 7 Oct** (judge panel: client knowledge is our weakest criterion) | Trades, Trading Notes, the facility gift |
| Q5 | Does the growth portion reduce risk ahead of 2033, and on what rule? | "Changing time horizons" (criterion 1) |
| Q6 | Promise lock calibration: how much is locked in 2031, how the range and confidence are stated. Principle decided 30 Sep. **Due 16 Oct** | Final Report, criterion 5 |
| Q7 | Does Laura's creative income being exposed to AI change a real allocation (Angle A)? If not, drop it. | Whether the thesis is specific to Laura |
| Q8 | Model upgrades: historical resampling of returns instead of the current simplified random returns; interest rates that move; costs and inflation. | Whether the numbers are publishable |
| Q9 | Which 3 Trading Notes go in the 23 Oct analysis? Means the trades behind them must be executed well before then. | Trading Notes Analysis |
