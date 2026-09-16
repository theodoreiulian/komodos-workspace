# KB2 — Portfolio construction toolkit

*The standard machinery, with a note on where each piece is genuinely useful for
Laura and where it is decoration. Judges reward tools that produce decisions.*

---

## 1. The asset-only core (Markowitz and its limits)

**Mean–variance optimisation (MVO)** picks weights maximising expected return per
unit of variance; the set of best portfolios is the **efficient frontier**.
Finale judges have explicitly praised efficient-frontier work (Vikas Keswani,
2024), so it is on-rubric.

**Use it for:** showing *why* our growth sleeve holds what it holds; showing the
cost of constraints; illustrating diversification benefit.

**Be honest about its weaknesses** (this is where we can outclass other teams —
most will present a frontier as if it were truth):
- MVO is **error-maximising**: it loads on whichever asset has the most
  over-estimated expected return. Expected returns are estimated with enormous
  error; covariances less so.
- It is **single-period**, so it says nothing about a six-year path to a dated
  goal. Laura's problem is multi-period and date-specific.
- It assumes **normal** returns. Real returns have fat tails and skew.
- It is **asset-only**: it cannot see the liability at all.
- Remedies worth knowing by name: **Black–Litterman** (blend equilibrium returns
  with our views), **resampled frontiers**, shrinkage estimators, and simple
  constraints (min/max weights) which usually beat optimisation.

> A team that presents a frontier looks competent. A team that presents a frontier
> *and explains why they did not simply obey it* looks like investors.

## 2. Risk decomposition

- **Volatility (σ)** — dispersion. Not risk itself; a proxy.
- **Correlation & covariance** — the engine of diversification. Correlations rise
  in crises, exactly when diversification is needed. Say this.
- **Beta** — sensitivity to the market. Useful for describing the growth sleeve.
- **Downside deviation / semivariance** — only counts bad outcomes. Better suited
  to Laura, whose loss function is one-sided.
- **Value at Risk / Conditional VaR** — loss at a percentile / average loss beyond
  it. CVaR is the honest one.
- **Maximum drawdown** — peak-to-trough. The number a real client actually feels.
- **Tracking error / surplus volatility** — for LDI, the one that counts (KB1).
- **Sharpe ratio** = (return − risk-free) ÷ σ. Careful: at a ~4.9% risk-free
  rate, Sharpe ratios look very different from the 2010s. **Sortino** uses
  downside deviation instead.

## 3. Factors

Beyond the market factor: **size**, **value**, **momentum**, **quality/
profitability**, **low volatility**, **investment**. Useful because they explain
*why* a set of holdings behaves as it does, and they let us describe a portfolio
in four words rather than twenty tickers. Relevant here: **quality** and **low
volatility** tilts historically deliver a smaller left tail per unit of expected
return — which is the trade Laura's asymmetric loss function actually wants.

## 4. Diversification, properly

WInS imposes no sector minimums, and Wharton warns against owning many securities
for its own sake: *"The goal is to build an intentional mix… not simply to own a
large number of securities."* Dimensions available to us:

asset class · sector/industry · market cap · geography · currency · duration and
credit · **funding purpose** (the LDI dimension, and the one that is
client-specific rather than generic).

Watch the **hidden concentration** problem: in 2026 the top three S&P 500 names
are >20% of the index, and a small group of companies has produced 65–75% of
index earnings growth since late 2022. "Buy the index" is no longer a
diversification decision — it is an active bet on the AI capex cycle. Saying that
out loud, with numbers, is a differentiator.

## 5. Rebalancing and glidepaths

- **Calendar** (e.g. annual) vs **threshold** (e.g. ±5 percentage points) vs
  **hybrid**. Threshold rebalancing is more responsive; calendar is cheaper and
  more disciplined. With a 200-trade cap and $25 commissions, cheap and
  disciplined wins in the simulator.
- **Glidepath** — the pre-committed shift from growth into matching assets. It
  can be **time-based** (mechanical, easy to communicate, ignores information) or
  **funded-ratio-based** (de-risk when you are far enough ahead — locks in luck,
  exactly the behaviour Laura's asymmetric loss function wants).
- Stating the glidepath as a **rule** in the IPS is how we satisfy "how will the
  portfolio's composition change as funding needs approach" *and* protect
  ourselves from the frozen-strategy trap: a rule adapts to outcomes without
  being a revision.

## 6. Human capital — the piece most teams will miss

Modern lifecycle theory (Merton; Bodie, Merton & Samuelson; Campbell & Viceira)
treats a person's **future earnings as an asset on their balance sheet** — often
the largest one — and concludes that the financial portfolio should be chosen
**relative to** it:

- If human capital is **bond-like** (a tenured salary), the financial portfolio
  can hold more equity.
- If human capital is **equity-like or sector-concentrated**, the financial
  portfolio should tilt *away* from that exposure. The canonical example: an
  employee should not hold their employer's stock — they are already maximally
  long it.

Laura's human capital is equity-like (lumpy advances, royalties, speaking fees,
licensing) **and** concentrated in creative IP, an industry currently being
repriced by generative AI. Two implications, both defensible and both specific
to her:
1. Her income is **volatile and positively correlated with the discretionary /
   media economy**, which argues for a genuinely defensive posture on the money
   that must fund a fixed obligation.
2. The financial portfolio can act as a **partial hedge** for the technological
   risk to her earnings. → developed in `../differentiation-angles.md`, Angle A.

2024 finale judge Zoe McCormick: *"When analyzing someone's investments, take a
look at this person holistically."* That is the human-capital argument in plain
English, from a judge.

## 7. Behavioural considerations

Relevant to how we advise, and worth a sentence because the case is explicitly
about a client's confidence:
- **Loss aversion** — losses hurt ~2× as much as equivalent gains. Laura's
  reputational loss from over-promising is a pure loss-aversion problem.
- **Mental accounting** — usually a bias; here it is *useful*, and it is the
  psychological basis of the two-portfolio structure. Bucketing lets a client take
  more risk in the growth sleeve because the essential goal is visibly safe.
- **Overconfidence / narrow framing** — the reason we pre-commit to rules.
- **Sequence-of-returns risk** — the order of returns matters when there are cash
  flows. See KB3.

---

## Quick reference: where each tool belongs

| Tool | Where it earns its place for Laura |
|---|---|
| Cash-flow matching / ladder | Operating reserve. The core of the answer. |
| Duration matching | Reserve, if we hold ETFs rather than individual bonds |
| Monte Carlo | Facility-contribution range and the confidence statement |
| Efficient frontier | Justifying the growth sleeve's composition |
| Factor tilts (quality, low-vol) | Shaping the growth sleeve's left tail |
| Human-capital analysis | Choosing what the growth sleeve must *avoid* — and hedge |
| Scenario analysis | "Under varying market outcomes" in the Final Report |
| Glidepath rule | Satisfies "how composition changes over time" in the IPS |
| Rebalancing policy | Discipline; also a good Trading Note subject |
