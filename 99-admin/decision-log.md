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

## 2026-10-21 — Build the ladder today at WInS prices; drop the Feb-2036 bond and pay 2037 from IBTQ
**Tier:** 2
**Status:** Decided
**Question:** The 2 Oct trades were never placed (WInS 0/200 on 21 Oct). The Trading
Notes Analysis (due 23 Oct) needs executed trades with notes. What exactly do we buy
today, and does the 30 Sep order list still hold at today's prices?
**Options considered:** A the 30 Sep design at today's prices ($215,564, 9 trades);
B drop the 4.500% 15-Feb-2036 bond and pay the 1 Jan 2037 bill from extra IBTQ
($213,976, 8 trades); C rush a Gift Portfolio (Q4) trade so one note shows growth.
**Decision:** B. Eight Promise Portfolio orders (list in
`04-portfolio/trading-notes-drafts.md`). Q4 is not rushed: the three notes for the
analysis come from the ladder (IBTO, IBTQ, T-BOND 3.125% 15-Nov-2041).
**Reasoning:** WInS prices the Feb-2036 bond at 103.164, a 4.19% yield, while the
next bonds yield 5.19% (2037) and 5.37% (2038). Buying it overpays for the same
safety. B is $1,588 cheaper and one trade fewer even though the IBTQ money for 2037
is assumed to sit a full year at 0%. C would put an untested allocation into the
record to fill a deliverable; the IPS (6 Nov) is where the Gift Portfolio must be right.
**Evidence:** `03-modeling/src/ladder_reprice_2026_10_21.py` (run output in its main()).
**Strongest objection and the answer:** *More of the ladder sits in one fund (IBTQ
$37.8k, two bills).* Accepted: IBTQ holds only US Treasuries; the 2% margin and a
positive running surplus every year remain. *All three notes are bonds, none shows
growth:* the reflections say plainly that the rest of the account is for growth and
that this is where Laura's risk lives.
**Revisit when:** WInS's Feb-2036 price comes back in line (yield within ~0.3 point of
its neighbours) before 6 Nov; or IBTQ's limit order does not fill.

---

## 2026-11-04 — Protect operations from actual contributions; moderate global growth; back sponsor promises before making them
**Tier:** 3
**Status:** Decided — framework adopted; operating audit, exact holdings and IPS submission remain unfinished. Partially reverses 30 Sep: withdraw literal all-ten-on-day-one lock and validated 100% success; retain operating-first hierarchy.
**Question:** What framework fits Laura, distinguishes the team through reasoning rather than thematic investments, and can be stated before the IPS freeze?
**Options considered:** all-safe surplus; moderate global-stock surplus; high-stock surplus; AI/art thematic tilt; unbacked forecast-based sponsor range; cash-backed lower-end budget with conditional upside. Also retain the old fully funded 2027 claim versus cash-feasible staging.
**Decision:** Adopt `02-strategy/strategy-2026-11-04.md`:
- Start operating protection using only the 2027 contribution; complete/repair it first with the 2028 contribution. Growth gets verified surplus only. Audit all payment dates and conservative fund proceeds; no borrowing, assumed stock-return rescue or outside funding.
- Within the Gift Portfolio, target 40% broad global stocks and 60% eligible short USD Treasuries/cash; annual review/rebalance after operating checks. No dedicated AI, arts or geographic theme.
- In 2031, recheck and repair operations first; put 75% of remaining Gift assets into cash, quote the net funded amount as the lower-end building budget, and leave 25% unpromised under the same 40/60 policy. Assume zero cash interest. These are policy choices, not optimal weights or confidence levels.
- In 2033, reserve first, first operating payment second, building gift afterward. Additional giving is capped at gains above the initial unpromised 2031 capital and remains discretionary after fresh checks. No guaranteed retained amount and no separately sized contingency/endowment fund.
- Operating deficits after 2031 use unpromised capital first, then reduce the building budget if necessary; disclose the changed range. The sponsor minimum is conditional, not an unconditional promise immune to operating risk.
- Final Report must calculate modeled dollar ranges and confidence for the actual gift within both bounds, including operating/flexibility failure branches, then explain how the fixed rule updates on observed 2031 wealth. Do not defer all numbers until real 2031.
**Reasoning:** The fixed annual bills and the discretionary building gift bear different risks. The 2031 sponsor announcement shortens the useful growth horizon and makes credibility part of the investment policy. Moderate surplus growth keeps ambition while limiting pre-announcement downside. Broad diversification is defensible without inventing Laura-specific AI income correlations.
**Evidence:** original case/guide/IPS and recorded criteria in `00-competition/`; `01-research/strategy-evidence-2026-11-04.md`; new script/output `strategy_policy_2026_11_04`; independent red-team, judge and rules notes in `.context/`. Normalized base maximum-gift ceilings at 40% stocks vs 60%: middle 87.1 vs 89.2 units, lower fifth percentile 71.2 vs 65.6 per 100 starting Gift units. Assumed returns, not market quotes or calibrated probabilities. All-safe wins downside; no dominance or optimizer claim.
**Correction:** legacy January-2027 ladder $319,892 exceeds available $300,000 by $19,892. `run_strategies` effectively financed that gap until 2028 and assigned success by construction. Its fund proceeds approximation did not validate the 2% cushion. Withdraw the day-one and validated-100% headlines; preserve old outputs and immutable executed Trading Notes as historical evidence.
**Strongest objection (red team) and the answer:** all-safe provides a steadier sponsor quote, whereas growth risk can hurt before 2031. Accepted tradeoff: 40% stocks is a deliberately limited growth choice, not mathematically necessary. The 75% cash rule is also chosen, not inferred from client utility. Red-team follow-up required post-2031 operating priority and a discretionary extra-gift ceiling; both incorporated. Judge review finds operating proof and authentic student experience still weak; these are outstanding work, not solved by narrative. Rules review passes framework conditional on these corrections, not trades or final submission.
**Revisit when:** before 6 Nov, staged operating audit fails, realistic costs/payout assumptions materially reduce surplus, or stronger joint tests reverse the tradeoff. After freeze, apply the fixed top-up, range-update and spending rules; do not redesign the IPS with hindsight.
**Brief:** `06-team/briefings/2026-11-04-back-the-promise.md` (beginner review completed; fixes incorporated before final handoff).

---

## 2026-11-04 — Submit the reviewed IPS through the Team Leader's account
**Tier:** Operating action — explicitly authorised by the Team Leader
**Status:** Complete; portal confirmation observed
**Decision/action:** Entered and saved the final 46-word pitch and 498-word
statement, read back the saved values and verified them against the reviewed
draft, marked the task complete, reviewed the attached existing roster and
submitted application2026-1052791973. No new personal fields or legal agreement
were required. Official roster team name verified as **Komodos**.
**Evidence:** `05-deliverables/02-investment-policy-statement/submitted.md` and
`submission-record.md`; `.context/ips-submission-confirmation-2026-11-04.png`
and matching accessibility text. Portal explicitly confirmed receipt of the IPS
on4Nov, approximately22:08–22:09CET.
**Limits:** no new portfolio orders and no certification of live operating/Gift
cash classification. Those implementation checks remain open before the freeze.
**Revisit when:** a portal receipt problem is reported; preserve the submitted
archive rather than silently rewriting its historical text.

---

## Open questions

Owned by Claude. Priority order and dates live in `99-admin/state.md`.

| # | Question | What depends on it |
|---|---|---|
| ~~Q1~~ | ✅ **Answered 29 Sep** — full 2033–42 ladder buildable; see `04-portfolio/wins-instruments.md`. Was: What can WInS actually trade? Individual Treasuries 2033–2042? STRIPS (bonds that pay one amount at maturity and nothing before)? Target-maturity bond ETFs (funds that hold bonds maturing in one year, then close and pay out)? | Whether a matched ladder can be built at all |
| ~~Q2~~ | ✅ **Decided 30 Sep**: structural. Lock all ten payments at the start. | — |
| ~~Q3~~ | ✅ **Decided 30 Sep**: all of it, at the start (1 Jan 2027 in the plan; now in WInS). | — |
| Q4 | **Framework decided 4 Nov:** 40% global stocks / 60% short USD Treasuries-or-cash within verified surplus. Exact eligible holdings and orders remain open. | Implementation before freeze |
| Q5 | **Decided 4 Nov:** operating checks annually; 2031 cash backing removes most risk from announced contribution; payment-near reserve becomes cash. | IPS and implementation |
| Q6 | **Policy decided 4 Nov:** 75% net cash backing / 25% unpromised; discretionary extra-gift ceiling. Full modeled dollar ranges, confidence and joint operating-failure analysis still required. | Final Report, criterion 5 |
| Q7 | **Decided 4 Nov:** drop personalized AI hedge and thematic tilt. Evidence does not establish Laura's income-stock correlation; use broad diversification and promise timing. | Client-specific reasoning |
| Q8 | **Urgent:** rebuild cash-feasible staged operating schedule; audit actual fund payouts/risks and buffer; correct simulator mapping. Then strengthen normalized mixture model with historical/parameter sensitivity and purchasing-power discussion. | Exact orders, funding claims, publishable projections |
| ~~Q9~~ | ✅ **Submitted 22 Oct**: IBTO, IBTQ, T-BOND 3.125% 15-Nov-2041. Was: Which 3 Trading Notes go in the 23 Oct analysis? Means the trades behind them must be executed well before then. | Trading Notes Analysis |
