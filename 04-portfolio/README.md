# Portfolio

Live record of the WInS portfolio. Trading opens **28 Sep 2026** and closes
**6 Nov 2026**, when the portfolio freezes permanently.

## How a trade happens

1. Claude decides the trade and writes, in the brief: ticker, buy/sell,
   quantity, order type, and the **exact Trading Note text**. `rules-auditor`
   checks it first.
2. A team member enters the order and pastes the note into WInS **word for word**.
3. At the same moment, they copy the note into `trading-notes.md` and add the fill
   (date, price, quantity) to `trade-log.md`.
4. If WInS rejects the order or the fill is very different from expected, don't
   improvise — record what happened in `trade-log.md`; Claude will re-decide.

## What lives here
- `wins-instruments.md` — what WInS actually lists (bonds, ETFs), checked on the platform
- `trade-log.md` — every trade: date, security, quantity, price, sleeve, rationale
- `trading-notes.md` — ⚠️ **the exact text entered in WInS**, copied verbatim.
  The Trading Notes Analysis requires notes reproduced exactly as they appear in
  the platform, and Wharton verifies this. Copy the text here at the moment of
  entry — do not reconstruct it later.
- `holdings.md` — current positions and sleeve allocation

## Constraints (from `../00-competition/competition-brief.md`)
200 trades max · stocks ≥$5 · ETFs · Treasuries from US/UK/DE/FR/IT/NL only ·
no margin, shorting, crypto or derivatives · ≤2× daily volume · $25 per stock
trade, $10 per bond trade.

## The shape of a good Trading Note
Wharton's own model note does five things in ~65 words: names the **instrument**,
its **role** in the portfolio, the **benefit**, **the risk it accepts**, and the
tie back to **strategy**. The risk sentence is the part most teams omit. Ours
always includes it.
