# Modelling

Every number that appears in a deliverable must come from here or from a cited
source. No orphan numbers.

## Contents
| File | Purpose |
|---|---|
| `src/laura_core_model.py` | The arithmetic skeleton of the client problem |
| `output/core_model_run.txt` | Saved output of the current run |

## `laura_core_model.py`

Pure Python 3, no dependencies. Run:
```bash
python3 03-modeling/src/laura_core_model.py
```

Four sections:
1. **Reserve cost** — PV at the start of 2033 of the ten-payment annuity-due, at
   discount rates 0–6%, with Macaulay duration (~4.1 yr at 4.5%).
2. **Deterministic accumulation** — 2033 portfolio value for constant returns
   2–9%, and the surplus over the reserve.
3. **Monte Carlo** — i.i.d. lognormal returns; distributions of the 2033 value,
   the 2031 value (the year Laura must quote a range) and facility capacity, for
   three illustrative growth portfolios.
4. **Defeasance benchmark** — cost at the start of 2027 of a Treasury ladder
   maturing 2033–2042, priced off the real par curve.

### Headline results (see `output/core_model_run.txt`)
- Reserve cost at a 4.5% discount rate: **$413,440**; duration ~4.14 years.
- Deterministic 2033 value at 6%: **$626,290** → surplus ~$212,850.
- Full defeasance from 2027 on the **15 Sep 2026** curve: **$301,264** — 100.4%
  of Laura's first contribution. On the 2 Jan 2026 curve it was $325,868.
- More equity risk raises median facility capacity ($172k → $241k) but drops the
  5th percentile from $40,877 to **$0**.

## ⚠️ Known limitations — fix before the Final Report
1. **I.i.d. lognormal returns** understate fat tails, volatility clustering and
   mean reversion. → block bootstrap from historical returns.
2. **The 2033 reserve discount rate is a single fixed input** and is the model's
   weakest assumption. → stochastic rates, or at minimum a sensitivity table.
3. **No glidepath.** The simulation holds one risk level for six years; our actual
   strategy will de-risk. → implement the glidepath rule once chosen.
4. **No fees, commissions, taxes or inflation** in the projection. Taxes are out
   of scope per the case; the others are not.
5. **No modelling of the 2031 promise decision** as a decision — only the
   distribution of the 2031 value.

## Conventions
- Scripts are self-contained and re-runnable; anyone on the team can reproduce
  any figure.
- Save output to `output/` and commit it, so a number in a draft can always be
  traced.
- Comment the *assumptions*, not the syntax. Assumptions are what judges ask about.
