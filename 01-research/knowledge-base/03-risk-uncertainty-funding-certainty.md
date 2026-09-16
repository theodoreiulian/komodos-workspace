# KB3 — Risk, uncertainty, and what "a high degree of funding certainty" means

*The case asks us to **define** the term, **evaluate** it, and **state the
assumptions** behind it. That three-part demand is unusual and it is where the
Portfolio Analysis criterion will be won or lost.*

---

## 1. Risk vs uncertainty (and why the distinction earns marks)

**Knight's distinction:** *risk* is measurable — we can put a distribution on it.
*Uncertainty* is not — model error, regime change, things not in the sample.

A Monte Carlo output of "94.3% probability of success" is a **risk** statement
that quietly implies an **uncertainty** claim it cannot support. Wade Pfau's work
in the *Journal of Financial Planning* showed these scores are extremely
sensitive to inputs — the gap between an 83% and a 91% score can turn on a 0.5%
change in the assumed expected return.

So the sophisticated move is to report the number **and** its fragility. Something
like: *"Under our assumptions the probability is 94%; halve the equity risk
premium and it is 86%; the cash-flow-matched portion is 100% under all of them,
because it does not depend on returns at all."* That last clause is why the LDI
structure is not just a strategy but a **communication advantage**.

## 2. Three distinct ways to define "high funding certainty"

We must pick one and defend it. They are not equivalent.

| Definition | What it means | Strength | Weakness |
|---|---|---|---|
| **A. Structural / defeasance** | The ten payments are matched by dated bond cash flows. No return assumption is required at all. | Certainty is *engineered*, not estimated. Immune to model error. Trivially explainable to Laura. | Costs the surplus; depends on sovereign credit; needs the instruments to exist |
| **B. Probabilistic** | P(all ten payments made) ≥ some threshold under simulation | Flexible; allows more growth | The threshold is arbitrary; the number is only as good as the assumptions; "95%" means a 1-in-20 chance of failing a *promise* |
| **C. Scenario/stress-based** | Payments survive a named set of adverse histories (2000–02, 2007–09, 1973–74, a 1970s-style inflation run, a Japan-style lost decade) | Concrete, intuitive, no false precision | Not exhaustive; no probability attached |

**Recommended posture (to be confirmed, not yet decided):** use **A as the
backbone** for the operating reserve and **B + C for the surplus and the facility
range**. That gives a genuinely honest sentence:

> "The ten payments do not depend on markets at all. What depends on markets is
> how large a gift Laura can make — and we can put a range on that."

Note the rhetorical asymmetry: most teams will report one probability for
everything. Splitting certainty by *goal* is both more correct and more
persuasive, and it answers the case's demand that the reserve "protect the
operating commitment while preserving flexibility."

## 3. Sequence-of-returns risk

With cash flows, the **order** of returns matters, not just the average. Two
paths with identical average returns produce different outcomes if money moves in
or out along the way.

For Laura it bites in two specific places:
1. **2028 contribution** — the $150,000 enters at one point in time. If the
   market has already run, she buys high.
2. **2033 and after** — the reserve is being drawn down. Selling growth assets to
   make payments during a drawdown permanently impairs the portfolio. *This is
   precisely the risk that cash-flow matching eliminates*, because the money for
   each payment is already the right size and matures on time. Sequence risk is
   the technical name for the thing the ladder kills.

Also note **point-in-time date risk**: the facility contribution is determined by
the portfolio value on **one specific date, 1 January 2033**, promised **two
years earlier on 1 January 2031**. Not an average. A bad Q4 2032 is not averaged
away by six good years. This is a strong argument for de-risking *before* 2033,
not at it.

## 4. Monte Carlo — how to do it credibly

Our implementation is `03-modeling/src/laura_core_model.py`. Current version uses
i.i.d. lognormal returns — deliberately simple and transparent for a first pass.
Before the Final Report we should upgrade it and *say* that we did:

- **Block bootstrap** from historical returns — preserves fat tails, volatility
  clustering and some mean reversion; no distributional assumption.
- **Stochastic rates**, since the reserve's cost in 2033 depends on the yield
  curve *then*. Right now this is a single-point assumption and it is the model's
  weakest link.
- **Report the assumptions in a table**: expected returns, volatilities,
  correlations, inflation, the discount rate, and their sources. Judges reward
  "reasonable assumptions" — which means *stated*, not *optimistic*.
- **Sensitivity/tornado analysis**: which assumption moves the answer most? (It
  will be the equity risk premium and the 2033 discount rate.) Showing this is
  more impressive than any single probability.

**What the current model already tells us** (50,000 paths, 4.5% reserve discount):

| Growth portfolio | P(2033 ≥ reserve) | Facility capacity p5 | median | p95 |
|---|---|---|---|---|
| Conservative µ5% σ7% | 98.8% | $40,877 | $172,199 | $340,547 |
| Balanced µ6.5% σ11% | 95.7% | $7,677 | $210,350 | $508,692 |
| Growth µ8% σ16% | 91.1% | $0 | $241,261 | $732,157 |

Read the p5 column. **More risk raises the median gift and destroys the floor.**
Since Laura's promise to co-sponsors lives in the left tail, this table is close
to being the whole argument.

## 5. Building the co-sponsor range

The 2031 statement is a **forecast of a 2033 value**, made two years out, with an
asymmetric penalty: over-promising costs credibility, under-promising costs only
a little goodwill. Standard practice — a symmetric 90% confidence interval around
the median — is the **wrong** answer, and most teams will give it.

Better constructions to evaluate:
- **Floor-anchored range:** bottom = a value we can nearly guarantee (e.g. the
  matched/defeased portion, or a p5–p10 outcome); top = a genuine but explicitly
  conditional upside. Communicated as *"at least X, and up to Y if markets are
  kind."*
- **Make the floor structural.** If part of the facility gift is itself held in
  matched bonds maturing in 2032, the floor stops being a percentile and becomes
  a fact. Laura can then say "at least X" and mean it literally. This is the
  single most client-serving idea in the case: **it converts a statistical promise
  into a keepable one.**
- **Asymmetric loss framing:** choose the floor by minimising expected
  reputational cost, not by hitting a round confidence number. State the
  reasoning.
- **Pre-commit to an update rule**: "Laura will reconfirm the figure in 2032 once
  the portfolio is substantially de-risked." Managing expectations over time is
  itself good advice and shows we thought past the deliverable.

## 6. Risks to name explicitly in the deliverables

Naming risks — including ones we accept — is a scoring behaviour; Wharton's own
model Trading Note contains a risk sentence.

| Risk | Bearing on Laura |
|---|---|
| Interest-rate risk | Reserve cost in 2033 depends on the curve then; ladder purchased earlier removes it |
| Reinvestment risk | Coupons between payment dates; zeros/STRIPS remove it |
| Sequence-of-returns risk | Sharpest 2031–33 and during drawdown |
| Equity drawdown / valuation risk | S&P 500 forward P/E ~19.7–22.4× in 2026; Shiller CAPE only higher once, before the dot-com collapse |
| **Concentration risk** | Top 3 names >20% of the S&P 500; 65–75% of index earnings growth from a handful of firms since Nov 2022 |
| **AI capex-cycle risk** | Hyperscaler capex ~$754bn in 2026 (+83% y/y), ~$905bn expected 2027, running at ~75% of their cash flow — a ratio last seen in the late 1990s |
| Inflation risk | Not on the reserve (payments are fixed nominal) — on the **facility cost** and Laura's real living standard. US CPI 3.4% y/y in Aug 2026 |
| Rate-hike / duration risk | Fed expected to hike in Sep 2026; 10y at 5.00%, highest since 2007 |
| Currency risk | Euro-area sovereigns in our permitted universe; TWD (~31/USD) for Taiwanese purchasing power |
| Sovereign credit risk | Italy vs Germany spreads are not decoration |
| Liquidity risk | Individual bonds vs ETFs; the 2× daily-volume cap in WInS |
| **Human-capital risk** | Generative AI and Laura's creative income — see Angle A |
| Model risk | Our own Monte Carlo. Say so. |
| Longevity of commitment | Payments run to 2042; funding past that is out of scope but worth one honest sentence |
