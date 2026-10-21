# Trading Notes Analysis: draft (due Fri 23 Oct 2026, 5:00 p.m. ET)

Status: **SUBMITTED 22 Oct 2026, 00:46 CEST** via SurveyMonkey Apply (application
2026-1052791973; task completed 00:45 CEST; "Application Submitted!" confirmation shown).
The text below is exactly what was submitted. All 8 trades filled on 21 Oct 2026. The three
notes below were checked by script against WInS > Trading Notes (`/account/tradenotes`)
and match character for character. Submit Thu 22 Oct via SurveyMonkey Apply.

Picked from the 8 Promise Portfolio trades, so that each shows a different part
of the decision process:
1. **IBTO**: the design (why a ladder, why funds, how the 2033 bill is paid).
2. **IBTQ**: the plan tested against real prices and changed (criterion 4).
3. **T-BOND 3.125% 15-Nov-2041**: the risk we accept, and why lock in now.

Word counts checked by script (limit 100 per reflection).

---

## Trading Note 1: IBTO (744 shares)

**Trading Note (exactly as in WInS):**
Buying IBTO, a fund of US Treasuries that closes and pays out in Dec 2033, to fund Laura's Jan 2034 residency payment. One rung of a bond ladder that locks in all ten payments now. A fund's payout is close to fixed, not exact, so the ladder is sized 2% above each bill. Ladder interest pays 2033.

**Reflection (97 words):**
Laura's ten $50,000 residency payments are fixed in dollars and must be funded with a high degree of certainty, so our strategy locks in all ten from the start with Treasuries that pay out before each bill. WInS lists no Treasury maturing between 2031 and 2036, so we used funds that hold only Treasuries and close in a set year. The 2033 bill needs no purchase: the ladder's interest before 2033 covers it. Our $300,000 account is Laura's $450,000 plan at two-thirds scale. With the promise locked, markets can change her facility gift, never the residency's funding.

---

## Trading Note 2: IBTQ (1,583 shares)

**Trading Note (exactly as in WInS):**
Buying IBTQ, a Treasury fund paying out Dec 2035, for Laura's 2036 AND 2037 payments. WInS prices the Feb-2036 bond we planned for 2037 at a 4.2% yield vs about 5.2% for similar bonds, so we skip it. This saves $1,588 even if cash waits a year at 0%. Risk: more of the ladder in one fund.

**Reflection (94 words):**
This decision tested our plan against real prices. Our 30 September plan used the February 2036 Treasury for the 2037 payment. On 21 October, WInS priced it at a 4.2% yield while similar Treasuries paid about 5.2-5.4%, so buying it meant overpaying for safety. Our model showed that extra IBTQ shares, paid out in December 2035, fund both 2036 and 2037 for $1,588 less and one fewer trade, even with that cash earning nothing for a year. The payments stay fully funded, and the saving stays in the growth money for Laura's facility gift.

---

## Trading Note 3: T-BOND 3.125% 15-Nov-2041 (33 units)

**Trading Note (exactly as in WInS):**
Buying $33,000 face of the 3.125% Treasury due 15 Nov 2041 for Laura's final (Jan 2042) residency payment. With it, all ten are locked in; the rest of the account is for growth. Its low coupon means most value comes at the end and its price swings most; we accept that as we hold to maturity.

**Reflection (97 words):**
This last rung completes the ladder: all ten payments are locked in. It has the lowest coupon, so most of its value comes at maturity and its price moves most when interest rates change. We accepted that because we will hold it to the end; a fall in its WInS price is a loss only if we sell. Locking far-off payments now made sense because Treasuries yielded about 5.5%, close to forecast stock returns, so risking promised money paid little. Laura takes thoughtful risks with the rest, where a bad year shrinks the gift, never the promise.

---

## Where each number comes from
| Number | Kind | Source |
|---|---|---|
| Ten $50,000 payments; $300,000 + $150,000 = $450,000 | Fact | Case study |
| Two-thirds scale | Our choice | Decision log, 30 Sep |
| 4.2%, 5.2–5.4%, about 5.5% yields | Market prices (WInS, 21 Oct) | `03-modeling/src/ladder_reprice_2026_10_21.py` |
| $1,588 saving, one fewer trade, 2033 covered by interest | Model output | same script |
| 2% margin | Our choice | Decision log, 30 Sep |
| "Forecast stock returns" | Someone else's forecast | Vanguard, Jan 2026: US 3.9–5.9% a year |
| No Treasury between 2031 and 2036 in WInS | Fact (WInS list) | `04-portfolio/wins-instruments.md` |
