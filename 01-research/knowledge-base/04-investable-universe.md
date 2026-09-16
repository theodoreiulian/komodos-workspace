# KB4 — The investable universe, and what each instrument is *for*

*Constrained by WInS rules. Every instrument below is checked against them.
Nothing here is a recommendation yet — this is the menu, with the job each item
could do.*

---

## What we may hold

| Allowed | Notes |
|---|---|
| **Cash** | Earns nothing in WInS; in the real strategy, money-market/T-bill yields are ~3.9–4.2% (Sep 2026) |
| **Stocks ≥ $5** | Any listed on WInS, US or international; $5 floor excludes penny stocks |
| **ETFs** | Any on WInS — the widest and most useful category |
| **Treasury bonds** | **US, UK, Germany, France, Italy, Netherlands only** |

**Forbidden:** margin, short selling, stock-secured debt, crypto, derivatives
(so no options, no futures, no hedging overlays — collars and puts are out;
protection must be built structurally, from bonds).

**Constraints:** 200 trades total; ≤ 2× a security's daily volume; $25/stock
trade, $10/bond trade.

⚠️ **To verify in the practice period (15–25 Sep):** exactly which bond maturities
WInS lists, whether **STRIPS / zero-coupon Treasuries** are available, whether
TIPS are listed as bonds or only reachable via ETFs, and whether the ETF universe
includes target-maturity bond ETFs (iBonds/BulletShares-style). **These answers
determine how literally we can implement a ladder, so check them first.**

---

## 1. The matching sleeve

**Individual Treasuries, laddered.** The purest expression of the strategy. Buy
maturities landing in each payment year, 2033–2042. Payment certainty becomes a
property of the *structure*, not of a forecast.
- *Pro:* exact cash-flow matching; no reinvestment risk if zeros; the story
  explains itself to a non-specialist in one sentence.
- *Con:* ten separate lines = ten trades and $100 of commission (trivially
  affordable against a 200-trade budget); availability of long maturities in WInS
  must be confirmed; coupon bonds leave small reinvestment residuals.
- *Current pricing:* 5y 4.83%, 7y 4.91%, 10y 5.00%, 20y 5.40% (15 Sep 2026).

**Target-maturity bond ETFs**, if available — funds holding bonds all maturing in
one year, then liquidating. A ladder in a box: a few trades instead of ten, with
near-identical behaviour. Check availability.

**Broad Treasury ETFs by duration band** — e.g. short (1–3y), intermediate
(3–7y / 7–10y), long (20y+). Easy, liquid, and **the instrument in Wharton's own
model Trading Note** ("an intermediate-term U.S. Treasury bond ETF"). But note
the difference: a *constant-maturity* ETF never matures, so it gives duration
matching, not cash-flow matching — the price is uncertain on any given date.
Worth being explicit about that distinction; it is exactly the kind of precision
that reads as expertise.
- The liability's Macaulay duration at the start of 2033 is ~4.1–4.2 years, which
  is squarely an intermediate-Treasury profile. Useful to know.

**TIPS / inflation-linked** — likely only via ETFs. **Deliberately probably
*not* needed for the reserve**, because the $50,000 payments are fixed nominal.
Reaching for TIPS here is a common reflex that would signal we had not read the
case carefully. They would be relevant if we chose to hedge Laura's *real*
purchasing power outside the reserve.

**European sovereigns (DE, FR, IT, NL).** Genuinely interesting, and a place an
international team has an edge. Bund yields are structurally below Treasuries;
BTPs (Italy) pay a credit spread; all introduce **unhedged EUR/USD risk** against
a USD-denominated liability — which for a matching sleeve is usually a *mistake*,
and saying clearly why is better than using them. Useful as a **deliberate
rejection** documented in a Trading Note, or as a small, explicitly-reasoned
diversifier in the growth sleeve. Gilts add GBP risk similarly.

## 2. The growth sleeve

**Broad equity index ETFs** — the default core. But see the concentration
warning: cap-weighted US indices in 2026 are an active AI bet (top 3 names >20%
of the S&P 500). Consider equal-weight, ex-mega-cap, or complementary exposures,
and *say why*.

**Factor / smart-beta ETFs** — quality, minimum volatility, dividend growth,
value. The relevant ones here are those that compress the left tail, since
Laura's loss function is one-sided.

**International developed & emerging equity ETFs** — real diversification of both
country and currency. In 2026 US equities are expensive relative to most of the
world (forward P/E ~19.7× on the index, ~22.4× on the cap-weighted measure
frequently quoted, vs ~17.0× equal-weight), which is a live argument, not a
platitude. A European team can write about this credibly.

**Thematic ETFs (AI, robotics, semiconductors, infrastructure, clean energy)** —
high-conviction, high-concentration, usually high-fee. Use only if the *thesis*
requires the exposure and the exposure is not already obtained more cheaply. If
we go anywhere near the AI theme it must be for the hedging reason in Angle A,
not because AI is popular.

**Individual stocks** — the only way to express a truly specific view, and the
only category where our own research is visible. Expensive in trades and in
attention. A small number of positions, each with a real thesis, beats twenty.
Note the ≥ $5 rule and the volume cap.

**Dividend / income equity** — a bridge between sleeves. Careful: dividend yield
is not a substitute for a matured bond, and dividends are cut in exactly the
scenarios where the payments matter most.

**Gold / commodity ETFs** — no cash flows, so no place in a matching sleeve;
arguably a diversifier in the growth sleeve. Must clear a high bar of
justification, not vibes.

**REIT ETFs** — an interesting, honest link to Laura's goal: the residency is, in
part, a *building*. Real-asset exposure partially tracks construction and
property costs, which is a real hedge for the facility contribution's purchasing
power. Rate-sensitive, which cuts both ways at 5% yields. Worth genuine analysis.

## 3. Instruments we must not use — and should say so
Options, futures, swaps, structured products, shorting, leverage, crypto. Since
derivative hedges are off the table, **all downside protection in this strategy
has to be structural** — cash-flow matching, allocation, and time. That
constraint is worth one sentence in the IPS: it turns a rule into a reason.

---

## Practical WInS notes
- **Six weeks is not a track record.** We are demonstrating a strategy, not
  running one. Trades should be few, deliberate and documented.
- **Commissions are real:** $25 per stock trade. Twenty positions costs $500 —
  0.17% of the portfolio — before any market moves. Rebalancing frequently is
  self-harm.
- **International orders clear end-of-day**; US after-hours orders fill at the
  next open. From France, queue orders in the evening; no need to be awake.
- **Trade count budget** (indicative, to revisit): ~10 for the matching sleeve,
  ~15–25 for the growth sleeve, the rest reserved for genuine strategy changes.
  Nowhere near 200. Using few trades is itself evidence of discipline and should
  be *stated* in the Final Report as a deliberate choice.
