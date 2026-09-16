# Macro snapshot — September 2026

*Compiled 16 Sep 2026, the fortnight before trading opens. This is the world our
WInS portfolio will be built in and the starting point for Laura's 2027–2033
projections. Refresh before the IPS (6 Nov) and again before the Final Report.*

---

## 1. Rates: the defining feature of this cycle

**US Treasury par yield curve, 15 September 2026** (source: treasury.gov; full
2026 series saved as `us-treasury-par-yield-curve-2026.csv`):

| 1m | 3m | 6m | 1y | 2y | 3y | 5y | 7y | **10y** | 20y | 30y |
|---|---|---|---|---|---|---|---|---|---|---|
| 3.93 | 4.11 | 4.17 | 4.39 | 4.67 | 4.76 | 4.83 | 4.91 | **5.00** | 5.40 | 5.36 |

For contrast, **2 January 2026**: 1y 3.47, 2y 3.47, 5y 3.74, 10y 4.19, 30y 4.86.

So 2026 has delivered a **bear steepening**: the 10-year is up ~80bp year to date
and has touched 5% — **the highest since July 2007** — while the front end has
risen less. The 10s–2s spread is modestly positive (~33bp) after flipping either
side of zero through the year.

**Policy:** fed funds has sat at **3.50–3.75% for all of 2026**. After the August
CPI print, markets put **~89–92%** odds on a **hike** at the September meeting —
which would be the first increase since July 2023. A hiking Fed is a genuinely
different regime from the one every recent competition cohort has written about.

**Inflation (August 2026, released 11 Sep):** headline CPI **+0.4% m/m, 3.4%
y/y**; core **+0.3% m/m, 2.4% y/y** — the lowest core reading since March 2021.
The split matters: sticky headline (energy, services) with decelerating core is
what has markets pricing a hike while the underlying trend improves.

### Why this dominates Laura's case
1. A ~4.8–5.0% risk-free rate makes **defeasing her promise cheap**: our model
   prices the full ten-payment defeasance at **$301,264** in 2027 versus $325,868
   on January's curve. Rate moves have handed her roughly $25,000 of free
   optionality in eight months.
2. It **collapses the opportunity cost of safety**. The historical equity risk
   premium over long Treasuries is ~3–5%; that is the entire compensation for
   accepting a 20%+ drawdown risk on money that has a deadline.
3. It creates **duration risk in the other direction**: if we hold long bonds and
   rates keep rising, mark-to-market losses appear in the six-week WInS window.
   Held-to-maturity matching is indifferent to this; a constant-maturity bond ETF
   is not. Worth a Trading Note.

## 2. Equities: expensive, and concentrated in one story

- **Valuation:** S&P 500 around **19.7× forward earnings** on ~$390 forward EPS;
  the cap-weighted forward P/E frequently quoted has risen ~40% to **22.4×**
  while the **equal-weight index sits near 17.0×**. The **Shiller CAPE has been
  higher only once — before the dot-com collapse.**
- **Concentration:** the **top three stocks are over 20% of the S&P 500**. A
  small group of companies has produced **65–75% of index earnings, profits and
  capital spending since ChatGPT launched in November 2022**.
- **The AI capex cycle:** consensus has the largest hyperscalers spending
  **~$754bn of capex in 2026, up 83% year on year**, and **~$905bn in 2027**.
  That spending is running at roughly **75% of those companies' cash flow** — a
  ratio commentators explicitly compare to telecoms and tech in the late 1990s.
- Sell-side framing for the rest of 2026 is a "controlled valuation reset": rising
  earnings offsetting multiple compression, with a wide plausible index range
  (one published band: ~6,900–8,450) driven mainly by long-term Treasury yields,
  earnings revisions and financial conditions.

### Reading it honestly
This is not a "the market is a bubble" note. Earnings are real and growing. But
two facts are simultaneously true and both belong in our analysis:
1. **"Buy the S&P 500" is no longer a diversification decision.** It is a
   concentrated position in the AI capital-expenditure cycle. Any team that
   describes an S&P 500 ETF as "broad diversification" in 2026 is describing a
   portfolio that no longer exists.
2. **Laura's own earnings are exposed to the same cycle, from the other side.**
   The capex funds the models that are repricing illustration and publishing
   work. Her human capital and a naive index portfolio are *not* independent —
   they are two ends of the same trade. → `../differentiation-angles.md`, Angle A.

## 3. Taiwan

Relevant because the residency will be there and its costs will be incurred in
TWD, even though the case denominates the commitment in USD.
- **TWD ~31/USD**, and projected to stay weak into year-end as the central bank
  prioritises exporter competitiveness; it touched ~31.7 in early March, its
  weakest since May 2025, on foreign equity selling.
- **Inflation ~1.67%** on the official DGBAS forecast — **below** the central
  bank's 2% alert threshold. Taiwanese inflation is *lower* than US inflation.
- Growth moderating to ~3.5% in 2026 after a very strong 2025.

**Implication:** a fixed USD payment stream buys *more* in Taiwan over time if
this differential persists (US CPI 3.4% vs Taiwan ~1.7%, with a soft TWD). This
partially offsets the fact that the $50,000 payments are not inflation-indexed —
a genuinely non-obvious, client-specific observation that most teams will miss
because they will treat "not inflation-adjusted" as a straightforward negative.
It deserves one careful, hedged paragraph: currency forecasts over 16 years are
worthless, so we would frame it as a *risk that cuts both ways*, not a plan.

## 4. What to re-check before each deliverable
- [ ] Treasury curve (re-download the CSV)
- [ ] Fed decision and dot plot; did September deliver the hike?
- [ ] Latest CPI print
- [ ] S&P 500 level, forward P/E, and the equal-weight gap
- [ ] Any break in the AI capex narrative (hyperscaler guidance is the tell)
- [ ] USD/TWD and Taiwanese CPI

## Sources
US Treasury daily par yield curve (treasury.gov, 2026 series) · Federal Reserve
H.15 · CNBC, CNN, NBC, Fox Business, HousingWire and TD Economics coverage of the
August 2026 CPI release (11 Sep 2026) · CNBC on the 10-year touching 5%
(14 Sep 2026) · Advisor Perspectives / ETF Trends Treasury yield snapshot
(11 Sep 2026) · J.P. Morgan *Eye on the Market* 2026 Outlook · Charles Schwab
2026 mid-year outlooks · Goldman Sachs S&P 500 outlook · State Street equity
outlook · InvestingSage US market outlook (Sep 2026) · TradingEconomics and
CommonWealth Magazine on Taiwan.
