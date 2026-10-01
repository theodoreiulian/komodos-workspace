# Primer C — What a target-maturity fund is (IBTO)

*For P4. Read this, then explain it to the team in 3 minutes, without notes.
Read Primer A first. Facts about the funds are from the iShares fact sheet and
our WInS check on 29 Sep (`04-portfolio/wins-instruments.md`).*

## First: what a fund is

A **fund** is a big pot of money from many people, used to buy many
investments at once. You buy **shares** of the pot, so you own a small slice of
everything in it.

An **ETF** (exchange-traded fund) is a fund whose shares you can buy and sell
during the day, like a company's stock. In WInS you trade ETFs on the
**Stocks/ETFs** page, not the Bonds page.

## What a target-maturity fund is

Most bond funds last **forever**: when their bonds mature, they buy new ones. So
you never know what the fund will be worth on a given date.

A **target-maturity fund** is different. It holds **only** US Treasuries that
mature in **one particular year**, and then, in **December of that year, it
closes and pays all the money back** to whoever owns its shares. It behaves like
one big bond with a known end date.

**IBTO** = *iShares iBonds Dec 2033 Term Treasury ETF*:
- holds US Treasuries that mature during 2033;
- pays out the interest it receives along the way, as monthly payments to its
  owners;
- **closes in December 2033 and pays everything back**;
- costs 0.07% a year to run: $70 a year on $100,000.

## Why we need them

WInS lists **no** US Treasury bond that matures between **15 Feb 2031** and
**15 Feb 2036**. But Laura has to pay $50,000 on **1 January 2033, 2034, 2035
and 2036**. The four funds fill that exact gap:

| Fund | Closes and pays out | Covers the payment on |
|---|---|---|
| IBTM | Dec 2032 | 1 Jan 2033 |
| IBTO | Dec 2033 | 1 Jan 2034 |
| IBTP | Dec 2034 | 1 Jan 2035 |
| IBTQ | Dec 2035 | 1 Jan 2036 |

### Example: the 1 January 2034 payment
If we want about **$50,000** available at the start of 2034, we buy enough IBTO
shares that, when the fund closes in December 2033, the payout is about $50,000.
Work backwards. Suppose the fund earns about 4% a year for the roughly 7 years
until it closes. Money that grows 4% a year for 7 years gets multiplied by
1.04⁷ ≈ 1.316. So to end with $50,000 we need about
$50,000 ÷ 1.316 ≈ **$38,000 today**. IBTO showed **$23.00** a share on 29 Sep,
so that is about $38,000 ÷ $23 ≈ **1,650 shares**. *The 4% and the 7 years are
example numbers to show the idea. The real share counts come from our model.*

## The honest catches
- It's a **fund**, not a single bond. It's very close to a bond, but its final
  payout depends on the fund's bonds as a group, not one exact $1,000 promise.
- It trades like a stock, so its **price wobbles every day**, just like a bond's
  (see Primer B). Held to December of its year, the wobbles wash out.
- Its buy and sell prices can be far apart when the US market is closed. We
  **only trade it during US market hours**, 15:30–22:00 French time, with a
  limit order (an order that sets the most we'll pay).

## Say it in one sentence
> IBTO is a fund of US government bonds that all mature in 2033, and it closes
> and hands the money back in December 2033, so it works like one bond with a
> known end date.
