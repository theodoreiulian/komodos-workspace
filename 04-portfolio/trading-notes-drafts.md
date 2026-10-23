# Trading Note drafts: Promise Portfolio, 21 Oct 2026

Nothing was traded on 2 Oct; WInS showed 0/200 trades on 21 Oct. These replace the
2 Oct drafts. Sizing: `03-modeling/src/ladder_reprice_2026_10_21.py`, option B
(the Feb-2036 bond is dropped; see the decision log, 21 Oct).

**WInS limit: 300 characters per note** (the counter in the order-confirmation
box reads "0/300"). Every note below is plain ASCII and under 300 characters,
checked by script. Type or paste each note **exactly**: the Trading Notes Analysis
must reproduce it word for word.

## Order list (enter after 15:30 French time, US market open)

| # | Page | Security | Qty | Order | Limit | ~Cost | Pays 1 Jan |
|---|---|---|---|---|---|---|---|
| 1 | Stocks/ETFs | IBTO | 744 shares | Limit, Good for Day | 23.29 | $17,238 | 2034 |
| 2 | Stocks/ETFs | IBTP | 735 shares | Limit, Good for Day | 24.40 | $17,846 | 2035 |
| 3 | Stocks/ETFs | IBTQ | 1,583 shares | Limit, Good for Day | 24.01 | $37,818 | 2036 + 2037 |
| 4 | Bonds | T-BOND 4.750% 15-Feb-2037 | 29 units | Buy | — | $28,492 | 2038 |
| 5 | Bonds | T-BOND 4.500% 15-May-2038 | 30 units | Buy | — | $28,596 | 2039 |
| 6 | Bonds | T-BOND 4.375% 15-Nov-2039 | 31 units | Buy | — | $28,962 | 2040 |
| 7 | Bonds | T-BOND 4.250% 15-Nov-2040 | 32 units | Buy | — | $29,189 | 2041 |
| 8 | Bonds | T-BOND 3.125% 15-Nov-2041 | 33 units | Buy | — | $25,709 | 2042 |
| | | **Total incl. $125 commissions** | | | | **$213,976** | |

- 1 bond unit = $1,000 face value (WInS shows "FACE VALUE $1,000.00").
- Limits are 0.5% above the last price. WInS shows a placeholder ask (IBTO 36.83)
  outside market hours; a market order could fill there. **Never use Market for funds.**
- The 2033 bill has no purchase: the ladder's interest paid before 2033 covers it
  (running surplus $8,065 after the 2033 bill, ⅔ scale).
- ~$86,000 stays cash for the Gift Portfolio (Q4).

## Notes (exact text)

### 1. IBTO
Buying IBTO, a fund of US Treasuries that closes and pays out in Dec 2033, to fund Laura's Jan 2034 residency payment. One rung of a bond ladder that locks in all ten payments now. A fund's payout is close to fixed, not exact, so the ladder is sized 2% above each bill. Ladder interest pays 2033.

### 2. IBTP
Buying IBTP, a fund of US Treasuries that pays out in Dec 2034, to fund Laura's Jan 2035 residency payment. Part of our ladder locking in all ten payments from day one. Rate moves will change its price, but we hold to the end, so only the final payout matters. Sized 2% above the bill.

### 3. IBTQ
Buying IBTQ, a Treasury fund paying out Dec 2035, for Laura's 2036 AND 2037 payments. WInS prices the Feb-2036 bond we planned for 2037 at a 4.2% yield vs about 5.2% for similar bonds, so we skip it. This saves $1,588 even if cash waits a year at 0%. Risk: more of the ladder in one fund.

### 4. T-BOND 4.750% 15-Feb-2037
Buying $29,000 face of the 4.75% Treasury due 15 Feb 2037. Its repayment plus interest funds Laura's Jan 2038 residency payment. Held to maturity, the payment is certain whatever markets do. Its price falls if rates rise; that only matters if we sell, and we plan to hold to the end.

### 5. T-BOND 4.500% 15-May-2038
Buying $30,000 face of the 4.5% Treasury due 15 May 2038 to fund Laura's Jan 2039 residency payment. It locks in about 5.4% a year, close to what stocks are forecast to earn but without their risk. Its price falls if rates rise; we hold to maturity, so the payment is fixed.

### 6. T-BOND 4.375% 15-Nov-2039
Buying $31,000 face of the 4.375% Treasury due 15 Nov 2039, which pays out about 7 weeks before Laura's Jan 2040 residency payment. A close match means little cash waits idle. Its price will swing with interest rates, but held to maturity it pays a known amount on a known date.

### 7. T-BOND 4.250% 15-Nov-2040
Buying $32,000 face of the 4.25% Treasury due 15 Nov 2040 to fund Laura's Jan 2041 residency payment, one rung of the ladder that locks in her promise. Long bonds swing more in price when rates move; we accept that because we will hold it to maturity rather than sell.

### 8. T-BOND 3.125% 15-Nov-2041
Buying $33,000 face of the 3.125% Treasury due 15 Nov 2041 for Laura's final (Jan 2042) residency payment. With it, all ten are locked in; the rest of the account is for growth. Its low coupon means most value comes at the end and its price swings most; we accept that as we hold to maturity.

## Sources for the numbers in the notes
- 4.2% / 5.2% / 5.4% / 5.5% yields, $1,588 saving: `ladder_reprice_2026_10_21.py` (WInS prices, 21 Oct).
- 2% margin, 2033 paid by interest: same script; convention from the 30 Sep decision.
- "Close to what stocks are forecast to earn": Vanguard 10-year forecasts, US
  3.9–5.9% a year (January 2026), cited in the 30 Sep brief.
