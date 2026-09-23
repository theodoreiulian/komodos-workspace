"""
Barbell vs. balanced: what does Laura actually give up by making the
residency promise certain on day one?

Companion to laura_core_model.py, which establishes:
  - reserve cost at start of 2033, 4.5%           = $413,440
  - cost to defease the whole promise at 2027     = $301,264 (curve of 15 Sep 2026)
  - balanced whole-portfolio facility gift, median  ~$210,350 at 95.7% funding

This script prices the alternative: spend the 2027 contribution defeasing the
ten payments outright, then run the 2028 contribution as a growth sleeve with
nothing to protect. The residency is then funded by construction, and the only
question left is the size of the facility gift.

Return conventions and lognormal parameterisation are copied from
laura_core_model.simulate() so the two sets of numbers are comparable.

CAVEATS, same as the core model: i.i.d. lognormal returns understate fat tails,
autocorrelation and regime risk. The $301,264 defeasance cost is the 15 Sep 2026
curve and will differ on the day we actually trade.
"""
import math
import random

DEFEASANCE_COST_2027 = 301_264   # laura_core_model.report_defeasance(), 15 Sep 2026 curve
CONTRIBUTIONS = 450_000
SEED = 20261216


def simulate(start: float, years: int, mu: float, sigma: float,
             n_sims: int = 100_000, seed: int = SEED) -> list[float]:
    """mu = expected ARITHMETIC annual return, sigma = annual stdev."""
    rng = random.Random(seed)
    m = math.log((1 + mu) / math.sqrt(1 + sigma ** 2 / (1 + mu) ** 2))
    s = math.sqrt(math.log(1 + sigma ** 2 / (1 + mu) ** 2))
    out = []
    for _ in range(n_sims):
        v = start
        for _ in range(years):
            v *= math.exp(rng.gauss(m, s))
        out.append(v)
    out.sort()
    return out


def pct(data: list[float], p: float) -> float:
    return data[int(p / 100 * (len(data) - 1))]


def money(x: float) -> str:
    return f"${x:,.0f}"


def main() -> None:
    free = CONTRIBUTIONS - DEFEASANCE_COST_2027

    print("=" * 78)
    print("BARBELL: defease the promise at start of 2027, grow what is left")
    print("=" * 78)
    print(f"  Defeased at start of 2027:   {money(DEFEASANCE_COST_2027)}")
    print(f"  Growth sleeve:               {money(free)} "
          f"({free / CONTRIBUTIONS:.0%} of contributions)")
    print("  Sleeve invested start of 2028; 5 years to the start of 2033.")
    print("  P(all ten $50,000 payments funded) = 100% BY CONSTRUCTION.")
    print("  The whole facility gift is the growth sleeve. Nothing else is at stake.\n")

    scenarios = [
        ("100% equity (mu 8.0%, sd 16%)", 0.080, 0.16),
        ("80/20       (mu 7.0%, sd 13%)", 0.070, 0.13),
        ("balanced    (mu 6.5%, sd 11%)", 0.065, 0.11),
    ]
    for name, mu, sd in scenarios:
        gift = simulate(free, 5, mu, sd)
        quote = simulate(free, 3, mu, sd)   # start 2028 -> start 2031, co-sponsor quote date
        print(f"  {name}")
        print(f"    2033 facility gift  p5/p25/p50/p75/p95: "
              f"{money(pct(gift, 5))} / {money(pct(gift, 25))} / {money(pct(gift, 50))} / "
              f"{money(pct(gift, 75))} / {money(pct(gift, 95))}")
        print(f"    2031 sleeve value   p5/p50/p95:         "
              f"{money(pct(quote, 5))} / {money(pct(quote, 50))} / {money(pct(quote, 95))}")
        print()

    print("=" * 78)
    print("THE COMPARISON THAT MATTERS")
    print("=" * 78)
    print("  Balanced whole-portfolio (laura_core_model.py, mu 6.5% sd 11%):")
    print("    funding certainty 95.73%   facility gift p5 $7,677   median $210,350")
    print("  Barbell, 100% equity sleeve (this script):")
    print("    funding certainty 100%     facility gift p5 $120,028 median $206,817")
    print()
    print("  Near-identical median gift. A floor 15x higher. Certainty instead of")
    print("  confidence. If this survives scrutiny it is the strategy - so the job")
    print("  now is to attack it, not admire it.")


if __name__ == "__main__":
    main()
