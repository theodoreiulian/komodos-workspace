# Primer B — Why a bond's price falls when interest rates rise

*For P4. Read this, then explain it to the team in 3 minutes, without notes.
Read Primer A first if you're not sure what a coupon or yield is. "Example"
numbers are invented to keep the arithmetic simple.*

## The idea in one picture

A bond's payments are **fixed forever** when it is created. Interest rates in the
market **are not**. When new bonds start paying more, nobody wants to pay full
price for an old bond that pays less, so the old bond's price has to fall until
it is just as good a deal as the new ones.

## One worked example

*Example numbers.* Last year you bought a bond for **$1,000**. It pays a **4%
coupon** ($40 a year) and has **1 year** left: in one year it will pay $40 +
$1,000 = **$1,040**.

Today, interest rates rise. Brand-new one-year bonds now yield **5%**.

Someone with $1,000 can now buy a new bond and get **$1,050** in a year
($1,000 × 1.05 = $1,050). Why would they pay you $1,000 for your bond, which only
pays $1,040? They won't.

What *would* they pay? The price that gives them the same 5%:

  price × 1.05 = $1,040  →  price = $1,040 ÷ 1.05 = **$990.48**

So your bond's price **fell from $1,000 to $990.48**, a loss of about 1%,
because rates went up by 1 percentage point.

If rates had **fallen** to 3% instead: $1,040 ÷ 1.03 = **$1,009.71**. The price
**rises**.

## Longer bonds move more

A bond with **10 years** left is stuck with its low coupon for 10 years, not one,
so the same rise in rates hits it much harder: roughly **8–9%** instead of 1%.
The number that measures this sensitivity is called **duration**: roughly, a
duration of 8 means "the price moves about 8% for every 1-point change in
rates".

## ⚠️ The part that makes it true: this only matters if you sell

In the example, if you **keep the bond for the last year**, you still get
exactly **$1,040**, whatever happened to its price in between. The price drop
is a real loss only if you sell early.

This is why a bond that matures right before a payment Laura has to make is safe
for that payment, even though its price will wobble every day in WInS.
**Wobbling prices in WInS are not losses to Laura's promise**, as long as we hold
to maturity.

## Words to know
- **Interest rate / market yield** — what brand-new bonds pay today.
- **Duration** — how much a bond's price moves when rates move; longer bonds
  have more.

## Say it in one sentence
> When new bonds pay more, old bonds get cheaper until they're just as good a
> deal. But if you hold a bond to the end, you still get exactly what it
> promised.
