# Brief — Lock in the promise now

**Decision date:** 30 Sep 2026 · **Decided by:** Claude (lead strategist) ·
**Decision log:** `99-admin/decision-log.md`, entry of 30 Sep ·
**Numbers from:** `03-modeling/src/thesis_decision_2026_09_30.py` → output in
`03-modeling/output/thesis_decision_2026_09_30_run.txt`

*Primers A–D in `06-team/primers/` go deeper on bonds, yields, bond prices,
target-maturity funds and sequence risk.*

### Words used in this brief
| Word | Meaning |
|---|---|
| **Bond** | A loan to the US government that you can buy and sell. It pays interest twice a year and pays back a fixed amount on a fixed date. |
| **Face value** | The amount a bond pays back at the end. We buy bonds in $1,000 pieces. |
| **Maturity / matures** | The end date, when the face value is paid back. |
| **Yield** | The yearly return you lock in by buying a bond at today's price and holding it to maturity. |
| **Ladder** | A set of bonds with different end dates, one for each bill, like the rungs of a ladder. |
| **Fund / ETF** | A pot of many investments you buy shares in. An ETF (exchange-traded fund) trades like a stock. |
| **IBTO, IBTP, IBTQ** | Funds holding only US government bonds that end in 2033, 2034 and 2035. Each closes in December of its year and hands the money back (Primer C). |
| **Median / "typical"** | The middle result: half the simulated futures do better, half worse. |
| **"Bad case"** | The result that only 1 simulated future in 20 does worse than. |
| **Laura's two contributions** | $300,000 on 1 Jan 2027 and $150,000 on 1 Jan 2028, $450,000 in total (*fact, from the case*). |
| **Co-sponsors** | Other people or organisations Laura asks to help pay for the building. |
| **Q4, Q5, Q6** | Open questions in our decision log. **P2, P3** are team tasks in the punchlist. |

### What kind of number is it?
| Number | Kind |
|---|---|
| Ten × $50,000, paid 1 Jan 2033–2042; contributions of $300,000 + $150,000 | **Fact** (the case) |
| Bond yields, bond and fund prices (29 Sep 2026) | **Market prices** (US Treasury, iShares) |
| Vanguard's 3.9–5.9% / 4.9–6.9% forecasts | **Someone else's forecast**, cited |
| Our stock scenarios: 4.5% / 6.5% / 9.5% a year | **Assumptions** (ours) |
| 2% safety margin, ⅔ scale in WInS, 60/40 placeholder, 75% lock, 1% limit | **Choices** (ours) |
| Every result in the tables | **Model output**: only as good as the assumptions above |

---

## 1. What I decided

**We lock in all ten of Laura's $50,000 payments right at the start, with US
government bonds that pay out just before each bill is due. Everything left over
is invested to grow, and it's that money alone that decides how big her gift to
the building will be.**

The portfolio therefore has two parts with two different jobs:

| Part | Its job | Can markets hurt it? |
|---|---|---|
| **Promise Portfolio** (about ⅔ of the money) | Pay the ten $50,000 bills, 2033–2042 | **No**, as long as we hold every bond to its end date |
| **Gift Portfolio** (about ⅓) | Grow the money for Laura's gift to the building in 2033 | **Yes**, this is the only place we take risk |

Plus one rule for later: **in January 2031, when Laura tells co-sponsors how much
she'll give, we lock in the bottom of that range too** (the "promise lock",
section 4).

---

## 2. Why, in plain words

### a) Locking in one payment: a worked example
Take the bill Laura must pay on **1 January 2040**.

A US government bond works like a loan with a fixed payback date (Primer A).
Today's market prices say that to have **$50,000 on 1 Jan 2040**, 13¼ years
from now, you need to put aside about **$24,491 today**. *(Market price from the
US Treasury's yield table of 29 Sep 2026: money locked up until 2040 earns about
5.53% a year.)*

Check it yourself: $24,491 × 1.0553^13.25 ≈ $24,491 × 2.04 ≈ **$50,000**.

That $24,491 isn't a hope. If we buy the bond and hold it to the end, the
government pays the $50,000 back whatever the stock market does in between.

### b) All ten payments
The same calculation for every bill (*market prices, 29 Sep 2026*):

| Bill on 1 Jan | Years from today | Yield | Cost today of $50,000 then |
|---|---|---|---|
| 2033 | 6.26 | 5.21% | $36,390 |
| 2034 | 7.26 | 5.26% | $34,465 |
| 2035 | 8.25 | 5.30% | $32,644 |
| 2036 | 9.25 | 5.34% | $30,894 |
| 2037 | 10.26 | 5.38% | $29,203 |
| 2038 | 11.26 | 5.43% | $27,570 |
| 2039 | 12.25 | 5.48% | $26,000 |
| 2040 | 13.25 | 5.53% | $24,491 |
| 2041 | 14.26 | 5.59% | $23,040 |
| 2042 | 15.26 | 5.64% | $21,651 |
| **Total** | | | **$286,348** |

Bills further away cost less today, because the money has longer to grow.

**From the ideal number to what we actually pay:**
1. **$286,348**: ideal cost today, from the table.
2. **$289,510**: the same, bought on 1 Jan 2027 when Laura's first money arrives.
3. **$319,892**: with the **real** bonds and funds WInS lists, at the higher
   "buy" price, in whole $1,000 pieces, **2% extra** as a safety margin (sized for
   $51,000 bills), and assuming any cash that waits between interest payments and
   bills earns **nothing** (deliberately cautious; in real life it would earn
   interest). That's Laura's whole first $300,000 plus about $20,000 of her
   second. Anything left over after 2042 goes back to Laura.
4. **$211,094 → about $211,500 in WInS**: the same ladder bought today, at ⅔
   scale ($316,642 × ⅔ = $211,094), plus commissions and rounding (section 5).

### c) Why now: safety is cheap in 2026
- **Safe bonds pay a lot right now.** The 10-year US government bond yields
  5.26% (29 Sep 2026), close to its highest in almost twenty years.
- **Stocks aren't expected to pay much more.** Vanguard, one of the world's
  largest fund managers, forecasts US stocks at about **3.9–5.9% a year** for
  the next ten years, and non-US stocks at **4.9–6.9%** (published January
  2026). That's roughly what the safe bonds pay, but with much more risk.

When risk isn't expected to pay much extra, you don't take it with money that's
already promised to someone.

### d) The comparison that decided it
**How the simulation works:** the computer invents **200,000 possible futures**
for 2027–2033. In each one, every year's stock return is picked at random around
an assumed average (central case **6.5% a year**) with a typical swing of **±16%**,
roughly how much stocks move in a normal year. Future bond yields are also
picked at random. Then it plays out each strategy in every future and counts
what happens.

I tested four ways of handling Laura's money this way. Each strategy paid the same real-world costs, and each used the same
2031 promise lock (except the last). Central forecast for stocks. For now the
Gift Portfolio is modelled as 60% stocks / 40% bonds, a placeholder until Q4:

| Strategy | All 10 payments made | Gift: bad case (only 1 in 20 futures is worse) | Gift: typical (median) |
|---|---|---|---|
| **Lock all now (our choice)** | **100%** | **$128,642** | $167,845 |
| Lock half now, rest in 2031 | 99.96% | $77,490 | $168,696 |
| Lock all, but only in 2031 | 96.34% | $12,724 | $170,397 |
| Lock nothing until 2033 | 93.37% | $0 | $169,718 |

**How to read it:**
- The **typical** gift is almost the same in every row: about $168,000–170,000.
- Locking everything now makes the **bad case** about $51,000 better than the
  next-best option, and it is the only row where **all ten payments are made in
  every single future**.
- "Lock nothing" misses at least one payment in about **1 future in 15**
  (100% − 93.37% = 6.63%). For a promise to a residency and its artists, that is
  not a "high degree of certainty".

*The stock forecast is an **assumption**. I also ran a pessimistic and an
optimistic one (section 3); the ranking on safety doesn't change.*

### e) How safe is "safe"? (so no judge catches us out)
- **US government default.** If the US government stopped paying its debts, the
  ladder would fail, but so would almost every other investment. That's why we
  call the ladder "safe" rather than "impossible to lose".
- **The three funds (IBTO, IBTP, IBTQ) are close to fixed, not exactly fixed.**
  They hold government bonds that all end in their year, but the final payout
  depends on the fund as a whole. That's why we add the 2% margin and count
  their interest as earning nothing while it waits.
- **The 2033 bill has no bond of its own.** The other bonds pay interest twice a
  year. By the end of 2032 that interest adds up to about **$69,700** (full-size
  plan), more than the $50,000 bill, even if the cash earns nothing while it
  waits. We keep that cash for the 2033 bill only.
- **Prices move every day.** If interest rates rise, our bonds show a loss in
  WInS. That loss is only real if we sell early, and we won't (Primer B).

### f) Why this is about *Laura*, not just any client
- **The payments are fixed in dollars, not adjusted for inflation** (case study).
  So an ordinary US government bond matches them exactly. Most clients' needs
  can't be matched this precisely, and Laura's can.
- **Her fear is breaking a promise.** The case says: "if Laura promises more
  than she can ultimately contribute, she could damage her credibility and lose
  the confidence or participation of co-sponsors." Our answer: every promise she
  makes is locked in the moment she makes it, the residency's running costs now
  and the co-sponsor number in 2031.
- ⚠️ **Honest gap:** the judge panel scored "client knowledge" as our weakest
  area. Nothing in the Gift Portfolio is specific to Laura yet. That is decision
  Q4, due **7 Oct**, and it will use your P2 readings of the case.

---

## 3. What we gave up

**The strongest argument against:** *"Laura is 'willing to take thoughtful
risks'. Locking two-thirds of her money in bonds is over-insurance, and it
throws away upside."*

What it costs, from the model:
- **If stocks do as forecast:** almost nothing. The typical gift is within about
  $2,600 of the other strategies.
- **If stocks do worse than forecast:** nothing at all. Locking all now gives
  the *highest* typical gift ($161,222 against $131,524 with no lock).
- **If stocks do as well as their long-run history** (optimistic case, about 9.5%
  a year): the typical gift is about **$178,000** instead of about **$231,000**
  with no lock. That's about $53,000 less.
- **The best outcomes are smaller.** In the central case our lucky-case gift (only
  1 future in 20 is better) is about $221,000, against about $436,000 with no
  lock.

**Why it lost:** the case says the ten payments must be funded "with a high
degree of certainty" and that we may not rely on outside money to do it. Only
one strategy makes them 100% certain, and it costs little or nothing in a
normal world. We give up the lucky top end, not the middle. Laura's risk-taking
still happens, in the Gift Portfolio, where a bad outcome means a smaller
building, never a broken promise.

**Second argument against:** *"The 2031 promise lock sells after a crash."* True:
if stocks fall hard in 2028–30, locking 75% of the Gift Portfolio in 2031 locks
that loss in. In the central case, the floor Laura could quote is below $100,000
in about **1 future in 5** if the Gift Portfolio is all stocks, and about **1 in
13** if it's 60% stocks / 40% bonds. So **how much** to lock in 2031, and how
risky the Gift Portfolio should be before then, are **not decided today**. They
are Q5/Q6, due 16 Oct.

---

## 4. The promise lock (the idea judges remember)

In January 2031 Laura has to tell co-sponsors how much she'll give in 2033. The
rule: **move a large share of the Gift Portfolio into 2-year government bonds
that mature just before 2033. The amount locked is the bottom of the range she
quotes.** The bottom can then never be broken, because it already exists as
bonds, not as a guess.

*Example (central case, typical future):* the Gift Portfolio is worth about
$150,000 in January 2031. Lock 75% of it = $112,500 in 2-year bonds at about
5.4% a year → $112,500 × 1.054² ≈ $112,500 × 1.111 ≈ **$125,000** guaranteed
in 2033. Laura says "at least about $125,000, and more if markets are kind."

The **principle** is decided. The **75% figure is a placeholder**: it gets
decided with Q6.

---

## 5. What I need from you

### Friday 2 Oct: build the Promise Portfolio in WInS

The WInS account ($300,000) represents Laura's whole plan ($450,000) at
**two-thirds scale**, so each bill becomes $33,333 in WInS. *(Our choice, so
judges see both parts of the plan in one account. In the real plan, Laura's
money is 100% bonds during 2027, until her second contribution arrives. We say
that openly.)*

**9 purchases, about $211,500 in total** ($211,386 of bonds and funds + $135
commissions). The remaining ~$88,500 stays as cash
until the Gift Portfolio is decided on 7 Oct.

| # | What to buy | Where in WInS | Quantity | ~Cost | Pays for (1 Jan) | Risk to name in the note |
|---|---|---|---|---|---|---|
| 1 | IBTO (iBonds Dec 2033 Treasury fund) | Stocks/ETFs | 743 shares | $17,104 | 2034 | It's a fund, not one bond: final payout close to, not exactly, fixed |
| 2 | IBTP (iBonds Dec 2034) | Stocks/ETFs | 682 shares | $16,436 | 2035 | Same; newer, smaller fund |
| 3 | IBTQ (iBonds Dec 2035) | Stocks/ETFs | 668 shares | $15,832 | 2036 | Same |
| 4 | T-BOND 4.500% 15-Feb-2036 | Bonds | $24,000 face | $22,965 | 2037 | Matures Feb 2036; there's no bond ending in late 2036, so the money waits 10½ months for the 1 Jan 2037 bill, earning nothing |
| 5 | T-BOND 4.750% 15-Feb-2037 | Bonds | $29,000 face | $28,098 | 2038 | Price falls if rates rise (only matters if we sell) |
| 6 | T-BOND 4.500% 15-May-2038 | Bonds | $30,000 face | $28,500 | 2039 | Same |
| 7 | T-BOND 4.375% 15-Nov-2039 | Bonds | $31,000 face | $28,501 | 2040 | Same; the longest bonds move the most |
| 8 | T-BOND 4.250% 15-Nov-2040 | Bonds | $32,000 face | $28,695 | 2041 | Same |
| 9 | T-BOND 3.125% 15-Nov-2041 | Bonds | $33,000 face | $25,255 | 2042 | Low interest rate, so most of its value comes at the very end |

**And the 2033 bill?** No purchase. The bonds above pay interest twice a year.
Everything they pay before 2033 adds up to about **$69,700** (full-size plan)
even if it sits in a drawer earning nothing, which is more than the $50,000
bill. **Rule:** that interest cash is reserved for the 2033 bill and never moves
to the Gift Portfolio.

⚠️ **Before entering anything:**
1. **Prices change daily.** On Friday morning Claude re-checks prices and
   updates this table. **Use Friday's table**, not this one.
2. **Bond units:** these quantities assume 1 WInS bond unit = $1,000 face value.
   Before submitting, check WInS's "Estimated Order + Accrued Interest" is close
   to the "~Cost" column. **If it's 10× or 100× off, stop and tell Claude.**
3. **Funds (rows 1–3):** only during US market hours (15:30–22:00 French time),
   as **limit orders** (an order that sets the most you'll pay) at no more than
   1% above the last price. A normal "market order" buys at whatever the seller
   asks, and if the asking price is silly, we'd overpay. On 29 Sep the gap between buy and sell prices looked
   huge outside market hours.
4. **Trading Notes:** one per trade, **written by us** (P3 in the session pack).
   The last column of the table is the risk each note must cover, in our own
   words, not copied.
5. **Volume rule:** we may not buy more than 2× a security's daily trading volume.
   Glance at each security's "Day's Volume" in WInS before ordering and write it
   in the trade log. Ours are tiny, but we need to have checked.
6. **Commission:** check that the first fund purchase is charged $25 (we assume
   funds count as stock trades) and each bond $10.

---

## 6. What would change my mind

- **WInS prices differ a lot from the ones used here** (total ladder above about
  $230,000 in WInS) → re-check before trading.
- **Interest rates fall sharply before we'd buy.** Lower rates make bonds more
  expensive (Primer B). If every rate were 1 percentage point lower, the real
  plan's ladder would cost about **$353,000**, leaving $450,000 − $353,000 ≈
  **$97,000** to grow, instead of $450,000 − $319,892 ≈ **$130,000**. Our rule: the promise gets paid for first, from the second
  contribution if needed, and the Gift Portfolio gets what's left. If the ladder
  ever cost more than ~$375,000, leaving under $75,000 to grow, I would reopen
  the decision.
- **Q4 finds that Laura's situation calls for more growth risk**, enough that
  "lock half now" beats "lock all now" on the gift *and* stays near 100% safe.
  (Today it doesn't: lock-half's bad case is $51,000 worse.)

---

## 7. Say it in one sentence

> *Laura's ten-year promise to the residency is locked in with government bonds
> from day one, so the markets can only decide how big the building gift is,
> never whether the residency can pay its bills.*

*(This sentence may be reused or adapted when Claude drafts the IPS pitch.)*

---

### Still open, with dates
| Q | Question | Due |
|---|---|---|
| Q4 | What's in the Gift Portfolio, and what makes it Laura's? | 7 Oct |
| Q5 | How the Gift Portfolio's risk changes before 2031 | 16 Oct |
| Q6 | The promise lock: how much, and how we state the range and our confidence | 16 Oct |
