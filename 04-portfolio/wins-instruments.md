# What WInS (StockTrak) actually lists

Checked by Claude in the team's StockTrak account (Komodos-10427064) via browser,
29 Sep 2026, US market closed. Read-only; no orders placed. Paths:
Portfolio Simulation → Make A Trade → **Bonds** (`/trading/bonds`) or
**Stocks/ETFs** (`/trading/equities`).

## Bonds page

The bond "type" dropdown has **one option only: "Treasury"**. There are **no
notes and no STRIPS** (bonds that pay one lump sum at maturity and nothing before).

### United States — 43 issues, all labelled T-BOND

| Maturity | Coupon | | Maturity | Coupon |
|---|---|---|---|---|
| 15-Feb-2026 ⚠️ already matured | 6.000% | | 15-May-2039 | 4.250% |
| 15-Nov-2026 | 6.500% | | 15-Aug-2039 | 4.500% |
| 15-Feb-2027 | 6.625% | | 15-Nov-2039 | 4.375% |
| 15-Aug-2027 | 2.250% | | 15-Feb-2040 | 4.625% |
| 15-Aug-2027 | 6.375% | | 15-Aug-2040 | 3.875% |
| 15-Nov-2027 | 6.125% | | 15-Nov-2040 | 4.250% |
| 15-Feb-2028 | 2.750% | | 15-Feb-2041 | 4.750% |
| 15-Aug-2028 | 5.500% | | 15-May-2041 | 4.375% |
| 15-Nov-2028 | 5.250% | | 15-Nov-2041 | 3.125% |
| 15-Feb-2029 | 5.250% | | 15-Feb-2042 | 3.125% |
| 15-Aug-2029 | 6.125% | | 15-Aug-2042 | 2.750% |
| 15-May-2030 | 6.250% | | 15-Feb-2043 | 3.125% |
| 15-Feb-2031 | 5.375% | | 15-May-2043 | 2.875% |
| **15-Feb-2036** | 4.500% | | 15-Aug-2043 | 3.625% |
| 15-Feb-2037 | 4.750% | | 15-Feb-2044 | 3.625% |
| 15-Feb-2038 | 4.375% | | 15-May-2044 | 3.375% |
| 15-May-2038 | 4.500% | | 15-Aug-2044 | 3.125% |
| | | | 15-Feb-2045 → 15-May-2048 | 8 more issues, 2.5–3.125% |

Data quirks: the Nov-2028 symbol code says `15022028`; the Nov-2046 code says
`15012046`. Check the fill carefully if we ever trade these.

**No US maturity between 15-Feb-2031 and 15-Feb-2036.**

### Other permitted countries (4 issues each; bought in their own currency)

| Country | Issues (maturity, coupon) |
|---|---|
| UK (Gilt) | 07-Dec-2028 6.000%; 31-Jan-2032 1.000%; 07-Jun-2032 4.250%; 31-Jan-2033 3.250% |
| Germany (Bund) | 15-Nov-2029 2.100%; 04-Jan-2030 6.250%; 04-Jul-2040 4.750%; 15-Nov-2048 1.250% |
| France (OAT) | 25-Oct-2031 5.750%; 25-Apr-2035 4.750%; 25-May-2043 2.500%; 25-May-2045 3.250% |
| Netherlands (DSL) | 15-Jan-2030 2.500%; 15-Jan-2037 4.000%; 15-Jan-2042 3.750%; 15-Jan-2054 2.000% |
| Italy (BTP) | 11-Jan-2029 5.250%; 05-Jan-2031 6.000%; 03-Jan-2040 3.100%; 09-Jan-2044 4.750% |

Laura's payments are in US dollars, so any non-US bond adds currency risk (the
exchange rate can move against us).

## Stocks/ETFs page — target-maturity Treasury funds

These are funds that hold US Treasuries all maturing in one year, then close in
December of that year and pay the money back to their holders. All four are
**tradable in WInS**:

| Ticker | Fund | Last price | Day's volume | Bid / ask shown |
|---|---|---|---|---|
| IBTM | iShares iBonds Dec 2032 Term Treasury ETF | $21.76 | 296,315 | 20.83 / 22.61 |
| IBTO | iShares iBonds Dec 2033 Term Treasury ETF | $23.00 | 420,496 | 22.02 / 23.98 |
| IBTP | iShares iBonds Dec 2034 Term Treasury ETF | $24.08 | 90,074 | 23.05 / 25.09 |
| IBTQ | iShares iBonds Dec 2035 Term Treasury ETF | $23.68 | 100,756 | 22.67 / 24.69 |

- **Volume cap:** we may trade at most 2× a security's daily volume. IBTP's lowest
  figure, 90,074 shares × $24.08 ≈ $2.17m/day, is far above anything we would
  buy. Not a constraint.
- ⚠️ **The bid/ask gap shown (~$2) is ~8% of the price** — almost certainly a
  closed-market placeholder. Re-check during US market hours (15:30–22:00 French
  time) and use **limit orders**, not market orders, for these.
- Invesco BulletShares **Treasury** ETFs only go out to 2031 (launched June 2026,
  per etfgi.com / etftrends.com); their 2033–35 funds are corporate bonds.
  Not needed.

## What this means (a fact about the market, not a strategy decision)

**A matched ladder for all ten payments can be built in WInS.** Each payment is
due 1 January; each piece below pays out shortly before it:

| Payment (1 Jan) | Covered by | Pays out |
|---|---|---|
| 2033 | IBTM | Dec 2032 |
| 2034 | IBTO | Dec 2033 |
| 2035 | IBTP | Dec 2034 |
| 2036 | IBTQ | Dec 2035 |
| 2037 | T-BOND 4.500% 15-Feb-2036 | Feb 2036 (≈10½ months early) |
| 2038 | T-BOND 4.750% 15-Feb-2037 | Feb 2037 |
| 2039 | T-BOND 4.375% 15-Feb-2038 or 4.500% 15-May-2038 | 2038 |
| 2040 | T-BOND 2039 issues (May / Aug / Nov) | 2039 |
| 2041 | T-BOND 2040 issues (Feb / Aug / Nov) | 2040 |
| 2042 | T-BOND 2041 issues (Feb / May / Nov) | 2041 |

Whether we *use* a ladder is still the open thesis question (Q2/Q3) — this only
removes the doubt about whether we *could*.

Sources for fund descriptions: iShares IBTO fact sheet
(ishares.com/us/literature/fact-sheet/ibto-ishares-ibonds-dec-2033-term-treasury-etf-fund-fact-sheet-en-us.pdf);
etfgi.com/news/stories/2026/06/invesco-increases-optionality-its-bulletshares-defined-maturity-etf-suite.
