# Investment thesis — working document

**Adopted 23 September 2026.** See `../99-admin/decision-log.md`, entry of the
same date, for the options considered and the counter-arguments on the record.

⚠️ **This is a working document, not deliverable prose.** The one-sentence
thesis below is a placeholder for structure only. The sentence that goes into
the IPS must be written by the team, in the team's own words. That is a
competition rule.

---

## The decision

We satisfy the case's demand that the ten payments be funded "with a high degree
of certainty" **structurally** — by holding assets whose cash flows land on the
payment dates — rather than **statistically**, by reporting a probability from a
simulation.

The portfolio therefore has two parts with two different jobs, and only one of
them carries market risk.

| Sleeve | Job | Risk it carries |
|---|---|---|
| **Defeasance sleeve** | Pay ten $50,000 bills, 2033–2042 | Essentially none once matched. Reinvestment risk is removed by maturity-matching; sovereign credit risk remains |
| **Growth sleeve** | Fund the facility gift | All of it — and it protects nothing, so it can be genuinely aggressive |

## Why this, in plain words *(structure — write your own version)*

The residency's ten years of operating costs are not exposed to markets. What
markets decide is how large a building Laura can help fund. We can put a range
on that, and a floor under it.

## The numbers behind it

All from `../03-modeling/`. Do not quote any figure here without re-running the
script that produced it.

- Cost to defease the entire promise at the start of 2027, on the 15 Sep 2026
  curve: **$301,264** — about 100.4% of the first contribution, leaving roughly
  a third of total capital free to grow.
- Facility gift, defeasance + 100% equity sleeve: p5 **$120,028**, median
  **$206,817**.
- Same gift under a balanced whole-portfolio approach: p5 **$7,677**, median
  **$210,350**, funding certainty 95.73%.
- The comparison in one line: near-identical median, a floor roughly fifteen
  times higher, certainty instead of confidence.

## What this decision resolves

- **"High degree of certainty" now has a definition we can defend out loud:**
  the payments do not depend on returns. We are not asking a judge to accept a
  probability threshold we chose ourselves.
- **The 2031 co-sponsor range gets a real floor.** Laura must quote a range two
  years before the reserve is struck; under this structure the bottom of that
  range is a number we can stand behind.
- **The discount rate stops being an assumption.** It is the yield on the bonds
  we actually bought.

## What is still open

These are the decisions that now matter. They are tracked in the open-questions
table in `../99-admin/decision-log.md`.

1. **Calibration (Q8).** Full defeasance at the start of 2027, or partial with a
   pre-committed glidepath? Full defeasance removes six years of compounding on
   two-thirds of the capital. This is the biggest remaining strategy question.
2. **Implementation (Q1).** What WInS actually lists. Individual Treasuries and
   STRIPS give an exact match; target-maturity bond ETFs give a close one; only
   generic bond funds would force a duration-matched approximation, which is a
   weaker claim and would have to be stated as such.
3. **Sleeve contents (Q9).** This is now the only place security selection
   lives, which makes it more important, not less.
4. **Sleeve glidepath (Q4).** Does the growth sleeve de-risk into 2033, and on
   what trigger? Note this is a different question from the reserve's own
   evolution, which the structure answers automatically.
5. **Over-fitting (Q7).** Still live. Adopting an idea is not the same as having
   tested it.

## The test this strategy must pass

From `README.md` in this folder — re-check at every fortnightly review:

1. Can it be stated in one sentence a judge would repeat back?
2. Does it fund the ten payments with a defensible definition of certainty?
3. Does it explain how the portfolio changes over time, as a **rule**?
4. Is it specific to Laura — or could it have been written about anyone?
5. Can it survive being frozen on 6 November and evaluated on 4 December?

⚠️ **Question 4 is the weak one.** A defeasance ladder could be built for any
client with a fixed nominal liability. What makes it Laura's is *why* certainty
matters here — a promise to co-sponsors and residents that is reputational
before it is financial. That connection is not yet made anywhere in this
document, and it needs to be.
