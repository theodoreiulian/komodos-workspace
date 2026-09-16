"""
Laura Gao core financial model - The Komodos
Wharton Global High School Investment Competition 2026-2027

Purpose: establish the ARITHMETIC SKELETON of the client problem so every later
strategy discussion argues about assumptions, not about numbers.

Timeline (per case study): Year 0 = 2026. Contributions/withdrawals occur at the
BEGINNING of the applicable year.
  2027 (Y1): +$300,000
  2028 (Y2): +$150,000
  2033 (Y7): establish operating reserve, then first $50,000 payment, then
             decide facility contribution
  2033-2042: ten annual $50,000 payments (fixed nominal, NOT inflation-adjusted)

Run:  python3 03-modeling/src/laura_core_model.py
"""
from __future__ import annotations
import math
import random

PAYMENT = 50_000.0
N_PAYMENTS = 10
C1, C1_YEAR = 300_000.0, 2027
C2, C2_YEAR = 150_000.0, 2028
RESERVE_YEAR = 2033
PLEDGE_YEAR = 2031  # year Laura must quote a range to co-sponsors


# --------------------------------------------------------------------------
# 1. The liability: what does the ten-payment promise actually cost?
# --------------------------------------------------------------------------
def reserve_cost(rate: float, payment: float = PAYMENT, n: int = N_PAYMENTS) -> float:
    """PV at the START of 2033 of an annuity-DUE of n payments (first paid immediately).

    This is the 'defeasance cost': the amount that, invested at `rate` with certainty,
    exactly funds all ten payments and leaves nothing over.
    """
    return sum(payment / (1.0 + rate) ** k for k in range(n))


def liability_duration(rate: float, n: int = N_PAYMENTS) -> float:
    """Macaulay duration (years) of the annuity-due. Drives the immunisation target."""
    pv = reserve_cost(rate, 1.0, n)
    weighted = sum(k * (1.0 / (1.0 + rate) ** k) for k in range(n))
    return weighted / pv


# --------------------------------------------------------------------------
# 2. Accumulation: what is the portfolio worth at the start of 2033?
# --------------------------------------------------------------------------
def deterministic_2033_value(annual_return: float) -> float:
    """Value at the BEGINNING of 2033 under a constant compound return."""
    years_c1 = RESERVE_YEAR - C1_YEAR   # 6
    years_c2 = RESERVE_YEAR - C2_YEAR   # 5
    return C1 * (1 + annual_return) ** years_c1 + C2 * (1 + annual_return) ** years_c2


# --------------------------------------------------------------------------
# 3. Monte Carlo: the distribution of the 2033 value and the facility capacity
# --------------------------------------------------------------------------
def simulate(mu: float, sigma: float, n_sims: int = 100_000, seed: int = 20261216,
             reserve_rate: float = 0.045) -> dict:
    """Lognormal i.i.d. annual returns. Deliberately simple and transparent:
    every assumption here is one we must be able to defend out loud.

    mu    = expected ARITHMETIC annual return of the growth portfolio
    sigma = annual standard deviation
    reserve_rate = risk-free rate assumed available in 2033 to lock the reserve
    """
    rng = random.Random(seed)
    cost = reserve_cost(reserve_rate)
    # lognormal parameters from arithmetic moments
    m = math.log((1 + mu) / math.sqrt(1 + sigma ** 2 / (1 + mu) ** 2))
    s = math.sqrt(math.log(1 + sigma ** 2 / (1 + mu) ** 2))

    v2033, v2031, capacity = [], [], []
    for _ in range(n_sims):
        v = C1
        for year in range(C1_YEAR, RESERVE_YEAR):          # 2027..2032 -> start of 2033
            if year == C2_YEAR:
                v += C2
            v *= math.exp(rng.gauss(m, s))
            if year == PLEDGE_YEAR - 1:                     # value at start of 2031
                v2031.append(v)
        v2033.append(v)
        capacity.append(max(0.0, v - cost))

    def pct(data, p):
        d = sorted(data)
        return d[max(0, min(len(d) - 1, int(p / 100 * len(d))))]

    return {
        "reserve_cost": cost,
        "p_fully_fundable": sum(1 for v in v2033 if v >= cost) / n_sims,
        "v2033": {p: pct(v2033, p) for p in (1, 5, 10, 25, 50, 75, 90, 95, 99)},
        "v2031": {p: pct(v2031, p) for p in (5, 25, 50, 75, 95)},
        "capacity": {p: pct(capacity, p) for p in (5, 10, 25, 50, 75, 90, 95)},
        "mean_2033": sum(v2033) / n_sims,
    }


def money(x: float) -> str:
    return f"${x:,.0f}"


if __name__ == "__main__":
    print("=" * 78)
    print("1. COST OF THE TEN-YEAR OPERATING COMMITMENT (valued at start of 2033)")
    print("   Ten payments of $50,000, first one immediate. Nominal total: $500,000.")
    print("=" * 78)
    print(f"{'discount rate':>14} | {'reserve cost':>14} | {'Macaulay dur.':>13}")
    for r in (0.00, 0.02, 0.03, 0.04, 0.045, 0.05, 0.055, 0.06):
        print(f"{r:>13.1%} | {money(reserve_cost(r)):>14} | {liability_duration(r):>10.2f} yr")

    print()
    print("=" * 78)
    print("2. DETERMINISTIC PORTFOLIO VALUE AT START OF 2033")
    print("   $300k invested start-2027 (6 yrs) + $150k start-2028 (5 yrs)")
    print("=" * 78)
    print(f"{'return':>8} | {'2033 value':>13} | {'surplus over reserve @4.5%':>28}")
    cost45 = reserve_cost(0.045)
    for g in (0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09):
        v = deterministic_2033_value(g)
        print(f"{g:>7.1%} | {money(v):>13} | {money(v - cost45):>28}")

    print()
    print("=" * 78)
    print("3. MONTE CARLO - illustrative growth portfolios (100,000 paths)")
    print("=" * 78)
    scenarios = [
        ("Conservative  (mu 5.0%, sd  7%)", 0.050, 0.07),
        ("Balanced      (mu 6.5%, sd 11%)", 0.065, 0.11),
        ("Growth-tilted (mu 8.0%, sd 16%)", 0.080, 0.16),
    ]
    for name, mu, sd in scenarios:
        r = simulate(mu, sd, n_sims=50_000)
        print(f"\n{name}")
        print(f"  reserve cost @4.5%:        {money(r['reserve_cost'])}")
        print(f"  P(2033 value >= reserve):  {r['p_fully_fundable']:.2%}")
        print("  2033 portfolio value  p5/p25/p50/p75/p95: "
              + " / ".join(money(r['v2033'][p]) for p in (5, 25, 50, 75, 95)))
        print("  2031 portfolio value  p5/p50/p95:         "
              + " / ".join(money(r['v2031'][p]) for p in (5, 50, 95)))
        print("  FACILITY CAPACITY     p5/p25/p50/p75/p95: "
              + " / ".join(money(r['capacity'][p]) for p in (5, 25, 50, 75, 95)))

    print()
    print("NOTE: i.i.d. lognormal returns understate fat tails, autocorrelation and")
    print("regime risk. Treat these as a SKELETON, not an answer. Before the Final")
    print("Report we should re-run with (a) block-bootstrapped historical returns and")
    print("(b) an explicit de-risking glidepath into 2033.")


# --------------------------------------------------------------------------
# 4. THE DEFEASANCE BENCHMARK  (added after seeing section 1-3 results)
# --------------------------------------------------------------------------
# What would it cost, at the start of 2027, to buy a Treasury ladder that
# defeases the ENTIRE ten-payment promise outright - i.e. zero market risk on
# the operating commitment, forever? Maturities needed: 6,7,...,15 years out.
# This is the single most useful reference number in the whole case. It converts
# "how much risk should Laura take?" into "what is Laura buying with the risk
# she takes?" - a question that can actually be answered.
def defeasance_cost_2027(curve: dict[int, float]) -> float:
    """curve: {years_to_maturity: zero/par yield}. Linearly interpolated."""
    def y(t: int) -> float:
        ks = sorted(curve)
        if t <= ks[0]:
            return curve[ks[0]]
        if t >= ks[-1]:
            return curve[ks[-1]]
        lo = max(k for k in ks if k <= t)
        hi = min(k for k in ks if k >= t)
        if lo == hi:
            return curve[lo]
        w = (t - lo) / (hi - lo)
        return curve[lo] * (1 - w) + curve[hi] * w
    return sum(PAYMENT / (1 + y(t)) ** t for t in range(6, 6 + N_PAYMENTS))


def report_defeasance():
    # US Treasury par yield curve, 15 September 2026 (source: treasury.gov)
    curve_20260915 = {1: 0.0439, 2: 0.0467, 3: 0.0476, 5: 0.0483,
                      7: 0.0491, 10: 0.0500, 20: 0.0540, 30: 0.0536}
    # January 2026, for contrast - shows how much the opportunity has improved
    curve_20260102 = {1: 0.0347, 2: 0.0347, 3: 0.0355, 5: 0.0374,
                      7: 0.0395, 10: 0.0419, 20: 0.0481, 30: 0.0486}
    print()
    print("=" * 78)
    print("4. THE DEFEASANCE BENCHMARK - cost at start of 2027 to lock the")
    print("   entire ten-payment promise with Treasuries maturing 2033-2042")
    print("=" * 78)
    for label, c in (("curve of 15 Sep 2026", curve_20260915),
                     ("curve of 02 Jan 2026", curve_20260102)):
        cost = defeasance_cost_2027(c)
        print(f"  {label}: {money(cost)}  "
              f"= {cost / C1:.1%} of the initial $300,000 contribution")
    cost = defeasance_cost_2027(curve_20260915)
    free = C1 + C2 - cost
    print()
    print(f"  Total contributions:                 {money(C1 + C2)}")
    print(f"  Cost to fully defease the promise:   {money(cost)}")
    print(f"  Capital left free to seek growth:    {money(free)}  ({free/(C1+C2):.0%})")
    print()
    print("  READ THIS CAREFULLY: at today's yields Laura could make her entire")
    print("  ten-year promise risk-free on day one for roughly the value of her")
    print("  first contribution, and still have ~1/3 of her capital to grow for")
    print("  the facility. Every unit of risk we take is therefore OPTIONAL and")
    print("  must be justified by what it buys her - a larger facility gift -")
    print("  not by the need to fund the residency. That is the strategy.")


if __name__ == "__main__":
    report_defeasance()
