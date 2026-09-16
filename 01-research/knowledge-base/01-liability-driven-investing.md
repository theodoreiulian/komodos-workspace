# KB1 — Liability-Driven Investing: the right frame for this case

*The single most important concept in the 2026–27 case. If we only master one
body of theory, it is this one.*

---

## Why LDI, and why it is unusual for a high-school team to say so

Most investing education is **asset-only**: maximise return for a given risk,
sit on the efficient frontier. That frame answers "how do I get rich?" It does
not answer "how do I make sure ten specific payments happen on ten specific
dates?"

Laura's case is the second question. The competition language gives it away:
*"support the ten-year operating commitment **with a high degree of certainty**"*
and *"teams may not rely on co-sponsors, grants, program fees, or other outside
funding."* That is the definition of a **liability**: a dated, quantified,
non-negotiable obligation.

Institutional finance has a whole discipline for this — **liability-driven
investing (LDI)**, used by defined-benefit pension funds and insurers. The core
move is to stop treating risk as "volatility of my assets" and start treating it
as **"the chance my assets fail to cover my liabilities"** — *surplus* risk.

> **The reframe:** Laura does not have one portfolio with one risk tolerance. She
> has a **liability to defease** and a **surplus to grow**, and they deserve
> opposite treatment.

---

## The vocabulary (use these precisely)

| Term | Meaning |
|---|---|
| **Liability** | A future payment we are committed to make. Here: 10 × $50,000, beginning-of-year 2033–2042. |
| **Defeasance** | Setting aside assets whose cash flows extinguish a liability, removing it from risk. |
| **Cash-flow matching (dedication)** | Buying bonds whose maturities/coupons land on the payment dates. Eliminates both interest-rate risk and reinvestment risk for those flows. The cleanest possible answer to "high degree of certainty." |
| **Immunisation** | Matching the **duration** (and ideally convexity) of assets to liabilities so that small parallel rate moves leave the surplus unchanged. Cheaper and more flexible than cash-flow matching, but only protects against parallel shifts, and must be rebalanced. |
| **Duration** | Sensitivity of value to interest rates; also the weighted-average time to the cash flows. |
| **Funded ratio** | PV(assets) ÷ PV(liabilities). Above 1.0 = surplus. |
| **Surplus risk** | Volatility of (assets − liabilities), not of assets. The *only* risk measure that matters for the reserve. |
| **Glidepath / de-risking** | A pre-committed rule that shifts assets from growth into matching as the funded ratio rises or as the payment dates approach. |

---

## The structure this implies: a two-portfolio (or "bucket") approach

Split Laura's money by **purpose**, not by asset class:

```
                     ┌─────────────────────────────────────┐
                     │  LIABILITY-MATCHING PORTFOLIO       │
                     │  Job: make ten payments happen.     │
                     │  Success = payments made. Not        │
                     │  return. Never return.              │
                     │  Tools: Treasury ladder / bond ETFs  │
                     │  matched to 2033–2042.              │
   Laura's capital ──┤                                      │
                     ├─────────────────────────────────────┤
                     │  SURPLUS / GROWTH PORTFOLIO          │
                     │  Job: make the facility gift bigger. │
                     │  Success = terminal value in 2033.   │
                     │  Can bear real equity risk because    │
                     │  failure here is disappointment,      │
                     │  not default.                        │
                     └─────────────────────────────────────┘
```

This structure is not a gimmick. It is **exactly** how a pension plan or an
insurer is run, it maps one-to-one onto the case's own two goals, and it
generates clean answers to every question the Final Report asks:

- *Reserve size?* = the defeasance cost of the ten payments.
- *Initial composition?* = matching assets.
- *How does composition change?* = it shortens mechanically as payments are made;
  the ladder self-liquidates. Nothing discretionary, nothing to get wrong.
- *What is "high certainty"?* = with cash-flow matching, it is not a probability
  at all — it is a **structural** guarantee, conditional only on sovereign credit.
- *Facility contribution?* = the surplus, minus a stated flexibility buffer.
- *Financial flexibility?* = a named, sized reserve we decline to give away.

Because the two sleeves have *different objectives*, they justify *different
risk levels* — which is how we answer "an appropriate balance between pursuing
growth and protecting the capital required for her goals" without hedging.

---

## Why 2026 makes this unusually powerful

The US Treasury par curve on **15 September 2026**: 1y 4.39%, 2y 4.67%, 3y 4.76%,
5y 4.83%, 7y 4.91%, 10y 5.00%, 20y 5.40%, 30y 5.36% — the 10-year at its highest
since 2007, with the Fed expected to **hike** (fed funds 3.50–3.75%, ~89–92%
market-implied odds of a September increase after a hot August CPI: headline
+0.4% m/m, 3.4% y/y; core +0.3% m/m, 2.4% y/y).

Two consequences:

1. **Defeasance is cheap.** Our model prices a 2027-purchased ladder maturing
   2033–2042 at **$301,264** for the whole $500,000 promise — versus $325,868 on
   the January 2026 curve. Roughly *one* of Laura's two contributions buys total
   certainty on the operating commitment.
2. **The opportunity cost of safety is low.** The classic argument against
   matching — "bonds yield nothing, you are wasting the growth years" — was true
   at 1.5% and is not true at 4.9%. The historical US equity risk premium over
   long Treasuries is on the order of 3–5%; at a 5% risk-free rate, the *expected*
   sacrifice from matching is small, while the *variance* reduction is total.

This is a genuinely time-specific argument. A team writing this strategy in 2021
would have been wrong. That is what makes it worth saying now.

---

## The important counter-arguments (steelman them; we will be asked)

1. **"Full defeasance in 2027 is over-insurance."** Laura says she is willing to
   take thoughtful risks and *wants* growth. A 100% matched reserve on day one
   removes six years of compounding on two-thirds of her money and shrinks the
   facility gift she cares about. **Response:** this is why the strategy should
   be a *glidepath*, not a one-shot decision — hold a growth allocation while the
   funded ratio is comfortable and de-risk on a pre-committed rule. But we should
   *price* full defeasance and show her what she is giving up, because that is
   what an honest adviser does.
2. **"Nominal matching ignores inflation."** Correct in general, wrong here: the
   case fixes the payments at $50,000 and explicitly says they are *not*
   inflation-adjusted. Nominal liabilities are matched by nominal bonds. Inflation
   attacks the *facility cost* and Laura's real living standard — different
   problem, different tool.
3. **"What about reinvestment of coupons?"** Real issue. Coupon-paying bonds
   create small reinvestment exposures between payment dates. Zero-coupon
   Treasuries (STRIPS) eliminate it; if WInS does not list STRIPS, we accept a
   small, *named* residual risk — naming it is itself a scoring behaviour (see
   the risk sentence in Wharton's model Trading Note).
4. **"Sovereign credit is not literally risk-free."** True; we say so. US
   Treasuries are the standard benchmark, and our permitted universe also
   includes UK, German, French, Italian and Dutch sovereigns, which carry
   *different* credit and currency profiles.

---

## Immediate implications for the WInS portfolio

The simulator runs **six weeks in 2026**, but the client invests in 2027. The
portfolio is a **demonstration**, not the real thing. So the portfolio should be
legible as a *scale model* of the strategy: a matching sleeve (Treasury bonds
and/or bond ETFs at the right part of the curve) and a growth sleeve, in the
proportions our strategy implies, with each trade's note stating which sleeve it
belongs to and what job it does there.

That also makes the Trading Notes Analysis almost write itself: pick one trade
from the matching sleeve, one from the growth sleeve, and one that *tested* the
strategy — ideally one where the evidence made us change our mind.

---

## Sources
- CFA Institute refresher readings: *Liability-Driven and Index-Based Strategies*;
  *Overview of Fixed-Income Portfolio Management*; *Principles of Asset Allocation*.
- CFA Level III curriculum notes on the goals-based approach and goals-based
  financial planning (AnalystPrep summaries).
- Financial Planning Association, *An Application of Asset-Liability Management
  for Financial Planners*.
- US Treasury daily par yield curve, 2026 series (saved:
  `01-research/market-context/us-treasury-par-yield-curve-2026.csv`).
- CNBC / CNN / TD Economics coverage of the August 2026 CPI release, 11 Sep 2026.
