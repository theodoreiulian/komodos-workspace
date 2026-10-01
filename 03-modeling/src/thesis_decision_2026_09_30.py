"""
Thesis decision model, 30 Sep 2026: how much of Laura's promise should be locked in, and when?

Built for decision Q2/Q3 in 99-admin/decision-log.md. It answers three questions:

  PART 1  What does it cost TODAY to lock in all ten $50,000 payments with bonds?
          (curve-based, and with the exact instruments WInS lists)
  PART 2  The exact WInS order list: the plan at 2/3 scale on the $300,000 account.
  PART 3  Three strategies for Laura's real money, compared under low / central /
          high stock-market assumptions:
            S1 LOCK ALL   - bond ladder for all ten payments at the start of 2027;
                            everything else in stocks ("growth sleeve")
            S2 LOCK HALF  - ladder for 2033-37 only; rest 60/40 until 2033, then buy
                            the 2038-42 payments at whatever rates are then
            S3 LOCK NONE  - 60/40 portfolio until 2033, then buy all ten payments
          plus the "promise lock" rule for the 2031 co-sponsor promise.

Run:  python3 03-modeling/src/thesis_decision_2026_09_30.py
Needs numpy (only for the Monte Carlo speed).

INPUT LABELS
  MARKET DATA  - a price or yield on a stated date, with source
  CONVENTION   - a choice we made
  ASSUMPTION   - a guess about the future
"""
from __future__ import annotations
import csv
import math
from datetime import date
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
TODAY = date(2026, 9, 30)                  # CONVENTION: settlement date for prices below
PAYMENT = 50_000.0
PAY_YEARS = list(range(2033, 2043))        # payments on 1 Jan of each year (case study)
SCALE_WINS = 2 / 3                         # CONVENTION: WInS $300k = Laura's $450k plan at 2/3 scale


def yf(d: date, start: date = TODAY) -> float:
    """Year fraction between two dates (actual/365.25)."""
    return (d - start).days / 365.25


# --------------------------------------------------------------------------------------
# PART 1a - zero-coupon ("spot") curve from the Treasury par curve
# --------------------------------------------------------------------------------------
# MARKET DATA: treasury.gov daily par yield curve, row for 29 Sep 2026
def load_par_curve(row_date: str = "09/29/2026") -> dict[float, float]:
    path = ROOT / "01-research/market-context/us-treasury-par-yield-curve-2026.csv"
    tenors = {"1 Mo": 1/12, "2 Mo": 2/12, "3 Mo": 0.25, "4 Mo": 4/12, "6 Mo": 0.5,
              "1 Yr": 1, "2 Yr": 2, "3 Yr": 3, "5 Yr": 5, "7 Yr": 7, "10 Yr": 10,
              "20 Yr": 20, "30 Yr": 30}
    with open(path) as f:
        for r in csv.DictReader(f):
            if r["Date"] == row_date:
                return {t: float(r[k]) / 100 for k, t in tenors.items() if r.get(k)}
    raise ValueError(f"{row_date} not in curve file")


def spot_curve(par: dict[float, float]):
    """Bootstrap semi-annual discount factors from par yields (linear interpolation
    of par yields between tenors). Returns a function t -> discount factor."""
    ts = sorted(par)
    def par_at(t):
        if t <= ts[0]:
            return par[ts[0]]
        for a, b in zip(ts, ts[1:]):
            if a <= t <= b:
                return par[a] + (par[b] - par[a]) * (t - a) / (b - a)
        return par[ts[-1]]
    grid = [0.5 * k for k in range(1, 61)]
    dfs = {}
    for t in grid:
        c = par_at(t) / 2
        if t <= 1.0:          # bills: treat as simple zero rates
            dfs[t] = 1 / (1 + par_at(t) / 2) ** (2 * t)
        else:
            dfs[t] = (1 - c * sum(dfs[s] for s in grid if s < t)) / (1 + c)
    def df(t: float) -> float:
        if t <= 0:
            return 1.0
        if t <= 0.5:
            return dfs[0.5] ** (t / 0.5)
        lo = max(s for s in grid if s <= t)
        hi = min(s for s in grid if s >= t)
        if lo == hi:
            return dfs[lo]
        # interpolate log discount factors
        w = (t - lo) / (hi - lo)
        return math.exp((1 - w) * math.log(dfs[lo]) + w * math.log(dfs[hi]))
    return df


# --------------------------------------------------------------------------------------
# PART 1b - the instruments WInS lists (04-portfolio/wins-instruments.md)
# --------------------------------------------------------------------------------------
# MARKET DATA: iShares product pages, 28 Sep 2026 (average yield to maturity; closing price)
# CONVENTION: net yield = YTM - 0.07% expense ratio; fund pays out 15 Dec of its year;
#             monthly distributions assumed reinvested in the same fund.
IBONDS = {  # payment year it funds : (ticker, price, ytm)
    2033: ("IBTM", 21.76, 0.0511),
    2034: ("IBTO", 23.02, 0.0514),
    2035: ("IBTP", 24.10, 0.0519),
    2036: ("IBTQ", 23.70, 0.0522),
}
# MARKET DATA: TreasuryDirect FedInvest, 29 Sep 2026. BUY price per $100 face (clean),
# accrued interest per $100. CONVENTION: we pay the buy (higher) price.
TBONDS = {  # payment year it funds : (WInS name, coupon, maturity, buy price, accrued)
    2037: ("T-BOND 4.500% 15-Feb-2036", 0.04500, date(2036, 2, 15), 95.1250, 0.563),
    2038: ("T-BOND 4.750% 15-Feb-2037", 0.04750, date(2037, 2, 15), 96.2969, 0.594),
    2039: ("T-BOND 4.500% 15-May-2038", 0.04500, date(2038, 5, 15), 93.3125, 1.688),
    2040: ("T-BOND 4.375% 15-Nov-2039", 0.04375, date(2039, 11, 15), 90.2969, 1.641),
    2041: ("T-BOND 4.250% 15-Nov-2040", 0.04250, date(2040, 11, 15), 88.0781, 1.594),
    2042: ("T-BOND 3.125% 15-Nov-2041", 0.03125, date(2041, 11, 15), 75.3594, 1.172),
}
COMMISSION_BOND, COMMISSION_ETF = 10.0, 25.0          # FACT: competition rules
OWN_SHARE = 0.70   # CONVENTION: see build_ladder()
BUFFER = 0.02      # CONVENTION: ladder sized for $51,000 a year - a 2% safety margin
PLAN_START = date(2027, 1, 1)   # FACT (case): Laura's first money arrives 1 Jan 2027
_DF = None         # set in main(): today's discount-factor function


def coupon_dates(maturity: date) -> list[date]:
    """Semi-annual coupon dates after TODAY, up to and including maturity."""
    out, d = [], maturity
    while d > TODAY:
        out.append(d)
        m = d.month - 6
        d = date(d.year - (1 if m <= 0 else 0), m + 12 if m <= 0 else m, d.day)
    return sorted(out)


def _cover(faces: dict, shares: dict, start: date = TODAY) -> dict:
    """Cash arriving for each 1 Jan payment from a given set of holdings.
    CONVENTION (cautious): every coupon waits as cash earning 0% until the next
    1 Jan payment; coupons paid before 2033 all count towards the 1 Jan 2033
    payment. So the ladder needs no assumption about future interest rates.
    Fund payouts on ~15 Dec of the fund's year. Funds are treated the SAME way as
    bonds: their monthly distributions also wait as cash at 0%, so a fund share is
    worth price x (1 + net yield x years) at the end (simple interest, no
    reinvestment). One rule for everything; no reinvestment-rate assumption."""
    cover = {y: 0.0 for y in PAY_YEARS}
    for y, face in faces.items():
        _, c, mat, _, _ = TBONDS[y]
        for d in coupon_dates(mat):
            if d <= start:
                continue                           # paid before we own it
            amt = face * c / 2 + (face if d == mat else 0)
            target = max(PAY_YEARS[0], d.year + 1)
            if target in cover:
                cover[target] += amt
    for y, n in shares.items():
        _, px, ytm = IBONDS[y]
        t = yf(date(y - 1, 12, 15), start)
        cover[y] += n * px * (1 + (ytm - 0.0007) * t)
    return cover


def build_ladder(payment: float, min_own_share: float = 0.0, start: date = TODAY,
                 buffer: float = 0.0) -> dict:
    """Cheapest cash-flow-matched ladder from the WInS instruments.

    Linear programme: choose how many $1,000 bonds of each T-bond and how many
    shares of each fund to buy, minimising today's cost, subject to: by each
    1 Jan payment date, the cash received so far (coupons, maturities, fund
    payouts; surplus carried forward at 0%) is at least the payments made so far.
    The solution is then rounded UP to whole bonds / shares and re-checked.
    Cash-timing conventions are in _cover()."""
    from scipy.optimize import linprog
    keys = [("T", y) for y in TBONDS] + [("I", y) for y in IBONDS]
    unit_cover, unit_cost = [], []
    for kind, y in keys:
        if kind == "T":
            cv = _cover({y: 1000}, {}, start)
            unit_cost.append(10 * (TBONDS[y][3] + TBONDS[y][4]))   # $ per $1,000 face
        else:
            cv = _cover({}, {y: 1}, start)
            unit_cost.append(IBONDS[y][1])
        unit_cover.append([cv[yy] for yy in PAY_YEARS])
    unit_cover = np.array(unit_cover)                    # instruments x years
    cum = np.cumsum(unit_cover, axis=1)                  # cumulative cash by year
    need = np.cumsum([payment * (1 + buffer)] * len(PAY_YEARS))
    A, b = -cum.T, -need
    if min_own_share > 0:
        # CONVENTION for the ladder we actually buy: every payment from 2034 on has
        # its own bond or fund that by itself pays at least `min_own_share` of that
        # bill. (2033 is paid by the coupons collected 2026-2032.)
        rows = []
        for i, (kind, y) in enumerate(keys):
            if y >= 2034:
                r = np.zeros(len(keys))
                r[i] = -unit_cover[i][PAY_YEARS.index(y)]
                rows.append(r)
        A = np.vstack([A, np.array(rows)])
        b = np.concatenate([b, -min_own_share * payment * np.ones(len(rows))])
    res = linprog(c=unit_cost, A_ub=A, b_ub=b, bounds=[(0, None)] * len(keys),
                  method="highs")
    assert res.success, res.message
    qty = np.ceil(res.x - 1e-9)
    faces = {y: int(q) * 1000 for (k, y), q in zip(keys, qty) if k == "T"}
    shares = {y: int(q) for (k, y), q in zip(keys, qty) if k == "I"}
    cover = _cover(faces, shares, start)
    carry, surplus = 0.0, {}
    for y in PAY_YEARS:
        carry += cover[y] - payment
        surplus[y] = carry
    assert min(surplus.values()) > -1, "rounded ladder is short"
    cost_t = sum(f / 100 * (TBONDS[y][3] + TBONDS[y][4]) for y, f in faces.items())
    cost_i = sum(n * IBONDS[y][1] for y, n in shares.items())
    if start != TODAY:
        # forward price: pay today's price less the coupons paid before `start`
        # (the later buyer doesn't get them), carried forward to `start`
        missed = sum(f * TBONDS[y][1] / 2 for y, f in faces.items()
                     for d in coupon_dates(TBONDS[y][2]) if d <= start)
        cost_t = cost_t - missed
        grow = 1 / _DF(yf(start)) if _DF else 1.0
        cost_t, cost_i = cost_t * grow, cost_i * grow
    nb = sum(1 for f in faces.values() if f)
    ne = sum(1 for n in shares.values() if n)
    comm = COMMISSION_BOND * nb + COMMISSION_ETF * ne
    return {"faces": faces, "shares": shares, "cost_t": cost_t, "cost_i": cost_i,
            "comm": comm, "total": cost_t + cost_i + comm, "leftover_2042": surplus[2042],
            "trades": nb + ne, "surplus": surplus, "lp_cost": res.fun}


# --------------------------------------------------------------------------------------
# PART 3 - Monte Carlo on Laura's real cash flows (v2, after red-team review 30 Sep)
# --------------------------------------------------------------------------------------
# Changes after the "too cautious" red team:
#  - S1 is charged the REAL ladder cost (WInS instruments, buy prices, coupons held at
#    0%) - the strictest basis for S1.
#  - Rivals buy their bonds later at the FORWARD rate implied by today's curve (fair to
#    them), with uncertainty around it.
#  - Every strategy gets the same 2031 promise-lock rule, so "promise kept" is equal
#    by construction and we compare what actually differs: certainty, floor, median.
#  - The growth part is tested both as 100% stocks and as 60/40.
# ASSUMPTIONS - stock market (global equities), arithmetic annual mean and volatility.
# Central is anchored on Vanguard's 2026 10-year forecasts (US 3.9-5.9%, non-US
# 4.9-6.9%, compound, published Jan 2026), converted to arithmetic by adding
# roughly sigma^2/2 (~1.3 points). "High" is close to the 1926-2025 US average.
EQUITY = {"low": (0.045, 0.16), "central": (0.065, 0.16), "high": (0.095, 0.16)}
BOND_6040 = (0.049, 0.06)      # ASSUMPTION: bond part earns ~today's 5-year yield
RATE_SD = 0.0125               # ASSUMPTION: uncertainty (1 sd) of future bond yields
LOCK_2031 = 0.75               # the promise-lock fraction (see brief for why 75%)
N_SIMS, SEED = 200_000, 20260930


def lognormal(rng, mu, sd, size):
    m = math.log((1 + mu) / math.sqrt(1 + sd ** 2 / (1 + mu) ** 2))
    s = math.sqrt(math.log(1 + sd ** 2 / (1 + mu) ** 2))
    return np.exp(rng.normal(m, s, size))


def pct(a, q):
    return float(np.percentile(a, q))


def forward_level_rate(df, buy_date: date, years: list[int]) -> float:
    """Single interest rate r at which buying these payments on buy_date costs the
    same as today's curve implies (forward cost). Found by bisection."""
    fwd_cost = sum(PAYMENT * df(yf(date(y, 1, 1))) for y in years) / df(yf(buy_date))
    lo, hi = 0.0, 0.2
    for _ in range(100):
        r = (lo + hi) / 2
        c = sum(PAYMENT / (1 + r) ** yf(date(y, 1, 1), buy_date) for y in years)
        lo, hi = (r, hi) if c > fwd_cost else (lo, r)
    return r


def cost_at(r, buy_date: date, years: list[int]):
    return sum(PAYMENT / (1 + r) ** yf(date(y, 1, 1), buy_date) for y in years)


def run_strategies(df, eq_key: str) -> dict:
    rng = np.random.default_rng(SEED)
    mu, sd = EQUITY[eq_key]
    eq = np.column_stack([lognormal(rng, mu, sd, N_SIMS) for _ in range(6)])   # 2027..2032
    bd = np.column_stack([lognormal(rng, *BOND_6040, N_SIMS) for _ in range(6)])
    mix = 0.6 * eq + 0.4 * bd
    t27 = yf(date(2027, 1, 1))
    one_year = df(t27) / df(yf(date(2028, 1, 1))) - 1
    two_year_2031 = (df(yf(date(2031, 1, 1))) / df(yf(date(2033, 1, 1)))) ** 0.5 - 1

    f31_all = forward_level_rate(df, date(2031, 1, 1), PAY_YEARS)
    f31_rest = forward_level_rate(df, date(2031, 1, 1), PAY_YEARS[5:])
    r31_all = np.clip(rng.normal(f31_all, RATE_SD, N_SIMS), 0.005, None)
    r31_rest = np.clip(r31_all - (f31_all - f31_rest), 0.005, None)
    y2 = np.clip(rng.normal(two_year_2031, RATE_SD, N_SIMS), 0.0, None)

    def lock_2031(v31, growth_31_33):
        """At 1 Jan 2031: LOCK_2031 of the growth money goes into 2-year Treasuries;
        that amount grown is the floor Laura quotes. Rest stays invested."""
        floor = LOCK_2031 * v31 * (1 + y2) ** 2
        return floor, floor + (1 - LOCK_2031) * v31 * growth_31_33

    out = {}
    # S1's ladder: real WInS instruments, bought 1 Jan 2027, 2% buffer, one 0%-cash rule
    real_ladder = build_ladder(PAYMENT, OWN_SHARE, PLAN_START, BUFFER)["total"]
    curve_2027 = sum(PAYMENT * df(yf(date(y, 1, 1))) for y in PAY_YEARS) / df(t27)
    # CONVENTION (fairness): every OTHER strategy's bond purchases cost the same % more
    # than the smooth curve as S1's real ladder does (instruments, buffer, idle cash).
    FRICTION = real_ladder / curve_2027
    for sleeve_name, g in (("100% stocks", eq), ("60/40", mix)):
        # ---- S1 LOCK ALL IN 2027 (real ladder cost) -------------------------------
        v = np.full(N_SIMS, 150_000 + (300_000 - real_ladder) * (1 + one_year))
        for j in (1, 2, 3):                       # 2028, 2029, 2030 -> start 2031
            v = v * g[:, j]
        floor, gift = lock_2031(v, g[:, 4] * g[:, 5])
        out[f"S1 lock all 2027, {sleeve_name}"] = dict(funded=np.ones(N_SIMS, bool),
                                                     gift=gift, floor=floor)
    # ---- S2 LOCK HALF IN 2027, 60/40, buy the rest + promise lock in 2031 ----------
    half = FRICTION * sum(PAYMENT * df(yf(date(y, 1, 1))) for y in PAY_YEARS[:5]) / df(t27)
    v = np.full(N_SIMS, 300_000 - half)
    for j in (0, 1, 2, 3):
        if j == 1:
            v = v + 150_000
        v = v * mix[:, j]
    rest = FRICTION * cost_at(r31_rest, date(2031, 1, 1), PAY_YEARS[5:])
    surplus = v - rest
    floor, gift = lock_2031(np.maximum(surplus, 0), mix[:, 4] * mix[:, 5])
    out["S2 lock half 2027, rest 2031"] = dict(funded=surplus >= 0, gift=gift, floor=floor)
    # ---- S3 LOCK NOTHING until 2031, 60/40, then buy all + promise lock -------------
    v = np.full(N_SIMS, 300_000.0)
    for j in (0, 1, 2, 3):
        if j == 1:
            v = v + 150_000
        v = v * mix[:, j]
    full = FRICTION * cost_at(r31_all, date(2031, 1, 1), PAY_YEARS)
    surplus = v - full
    floor, gift = lock_2031(np.maximum(surplus, 0), mix[:, 4] * mix[:, 5])
    out["S3 lock all in 2031"] = dict(funded=surplus >= 0, gift=gift, floor=floor)
    # ---- S4 LOCK NOTHING until 2033 (the original "no lock" 60/40) ------------------
    v = np.full(N_SIMS, 300_000.0)
    for j in range(6):
        if j == 1:
            v = v + 150_000
        v = v * mix[:, j]
    f33 = forward_level_rate(df, date(2033, 1, 1), PAY_YEARS)
    r33 = np.clip(rng.normal(f33, RATE_SD, N_SIMS), 0.005, None)
    full33 = FRICTION * cost_at(r33, date(2033, 1, 1), PAY_YEARS)
    s4 = v - full33
    out["S4 lock nothing until 2033"] = dict(funded=s4 >= 0, gift=np.maximum(s4, 0),
                                              floor=np.zeros(N_SIMS))
    meta = dict(real_ladder_2027=real_ladder, f31_all=f31_all, f33=f33,
                two_year_2031=two_year_2031, friction=FRICTION, curve_2027=curve_2027)
    return out, meta


def fmt(x):
    return f"${x:,.0f}"


def main():
    global _DF
    par = load_par_curve()
    df = spot_curve(par)
    _DF = df

    print("=" * 86)
    print("PART 1  Cost today (30 Sep 2026) of locking in all ten $50,000 payments")
    print("=" * 86)
    print("Par curve 29 Sep 2026 (treasury.gov):",
          ", ".join(f"{k:g}y {v*100:.2f}%" for k, v in sorted(par.items()) if k >= 1))
    total_curve = 0.0
    print(f"\n  {'Payment':<12}{'Years away':>11}{'Spot yield':>12}{'Discount factor':>17}{'Cost today':>13}")
    for y in PAY_YEARS:
        t = yf(date(y, 1, 1))
        d = df(t)
        spot = d ** (-1 / t) - 1
        total_curve += PAYMENT * d
        print(f"  1 Jan {y:<6}{t:>11.2f}{spot*100:>11.2f}%{d:>17.4f}{fmt(PAYMENT*d):>13}")
    print(f"  {'TOTAL (curve)':<52}{fmt(total_curve):>13}")
    t27 = yf(date(2027, 1, 1))
    print(f"  Same cost moved to 1 Jan 2027 (Laura's first money arrives): "
          f"{fmt(total_curve / df(t27))}")
    print("  For comparison: 15 Sep 2026 curve gave $301,264 at 1 Jan 2027 (laura_core_model.py)")

    lad = build_ladder(PAYMENT)
    lad_clean = build_ladder(PAYMENT, min_own_share=OWN_SHARE)
    print(f"\n  With the exact WInS instruments (buy prices, whole bonds, commissions): "
          f"{fmt(lad['total'])}")
    print(f"    T-bonds {fmt(lad['cost_t'])} + iBonds funds {fmt(lad['cost_i'])} "
          f"+ commissions {fmt(lad['comm'])}; left over after the last payment "
          f"{fmt(lad['leftover_2042'])} (rounding buffer)")
    print(f"  Ladder we buy - every bill from 2034 has its own bond/fund paying >= "
          f"{OWN_SHARE:.0%} of it: {fmt(lad_clean['total'])}"
          f"  (extra vs cheapest: {fmt(lad_clean['total'] - lad['total'])}; "
          f"left over after 2042: {fmt(lad_clean['leftover_2042'])})")
    plan = build_ladder(PAYMENT, OWN_SHARE, PLAN_START, BUFFER)
    print(f"  THE PLAN'S LADDER (bought 1 Jan 2027, sized for $51,000/yr = 2% buffer): "
          f"{fmt(plan['total'])} = {plan['total'] / 300_000:.1%} of Laura's first $300,000")
    print("  If rates fall before 1 Jan 2027 (whole curve shifted, same % friction):")
    fr = plan['total'] / (total_curve / df(t27))
    for shift in (-0.01, -0.005, 0.005):
        df_s = spot_curve({k: v + shift for k, v in par.items()})
        c = sum(PAYMENT * df_s(yf(date(y, 1, 1))) for y in PAY_YEARS) / df_s(t27) * fr
        print(f"    {shift*100:+.1f} points: ladder ~{fmt(c)}  -> money left for growth "
              f"~{fmt(450_000 - c)} (was {fmt(450_000 - plan['total'])})")
    print("\n  How each bill is paid (full scale, $):")
    cv = _cover(lad_clean['faces'], lad_clean['shares'])
    carry = 0.0
    for y in PAY_YEARS:
        carry += cv[y] - PAYMENT
        print(f"    1 Jan {y}: cash arriving in the 12 months before {fmt(cv[y]):>10}"
              f"   running surplus after paying {fmt(carry):>9}")

    print("\n" + "=" * 86)
    print(f"PART 2  WInS order list - the plan at 2/3 scale "
          f"(each payment ${PAYMENT*SCALE_WINS:,.0f})")
    print("=" * 86)
    lw = build_ladder(PAYMENT * SCALE_WINS, OWN_SHARE, TODAY, BUFFER)
    print(f"  {'Funds payment':<15}{'Instrument':<32}{'Quantity':>20}{'Est. cost':>13}")
    for y in PAY_YEARS:
        if y in lw["shares"]:
            tic, px, _ = IBONDS[y]
            n = lw["shares"][y]
            print(f"  1 Jan {y:<9}{tic + ' (Stocks/ETFs page)':<32}{n:>13,} shares{fmt(n*px):>13}")
        else:
            name, _, _, bp, ai = TBONDS[y]
            f = lw["faces"][y]
            print(f"  1 Jan {y:<9}{name:<32}{f'${f:,.0f} face':>20}{fmt(f/100*(bp+ai)):>13}")
    print(f"  {'Commissions ($10 per bond trade, $25 per ETF trade; ' + str(lw['trades']) + ' trades)':<67}{fmt(lw['comm']):>13}")
    print(f"  {'TOTAL LADDER':<67}{fmt(lw['total']):>13}")
    print(f"  {'Left for the growth sleeve (of $300,000)':<67}{fmt(300_000 - lw['total']):>13}")
    print("  (T-bond face assumes WInS bonds trade in $1,000 units - CHECK the 'Estimated")
    print("   Order' figure in WInS matches the cost column before submitting.)")

    print("\n" + "=" * 86)
    print("PART 3  Laura's real money - strategies compared on the strictest basis for S1")
    print("=" * 86)
    for key in ("low", "central", "high"):
        mu, sd = EQUITY[key]
        res, meta = run_strategies(df, key)
        if key == "low":
            print(f"  S1 ladder, real cost moved to 1 Jan 2027: {fmt(meta['real_ladder_2027'])}"
                  f" | forward rate for buying in 2031: {meta['f31_all']*100:.2f}%,"
                  f" in 2033: {meta['f33']*100:.2f}% | 2-yr rate implied for 2031: "
                  f"{meta['two_year_2031']*100:.2f}%")
            print(f"  Smooth-curve cost at 1 Jan 2027: {fmt(meta['curve_2027'])}; real ladder is "
                  f"{meta['friction']-1:.1%} more - every strategy's bond purchases are charged the same %.")
            print(f"  Every strategy uses the same 2031 promise lock ({LOCK_2031:.0%} of growth"
                  f" money into 2-year Treasuries), except S4.")
        print(f"\n  Stock assumption: {key.upper()}  (arithmetic mean {mu*100:.1f}%, "
              f"volatility {sd*100:.0f}%)")
        print(f"    {'Strategy':<36}{'All 10 paid':>12}{'Gift p5':>10}{'median':>10}"
              f"{'p95':>10}{'2031 floor p5':>15}{'floor median':>14}{'floor<$100k':>13}")
        for k, r in res.items():
            low_floor = np.mean(r['floor'] < 100_000) * 100 if 'S4' not in k else float('nan')
            print(f"    {k:<36}{np.mean(r['funded'])*100:>11.2f}%"
                  + "".join(f"{fmt(pct(r['gift'], q)):>10}" for q in (5, 50, 95))
                  + f"{fmt(pct(r['floor'], 5)):>15}{fmt(pct(r['floor'], 50)):>14}"
                  + f"{low_floor:>12.1f}%")

    print("\n" + "=" * 86)
    print("STRESS  Stocks fall 35% in 2032 (after the 2031 promise), central otherwise")
    print("=" * 86)
    res, _ = run_strategies(df, "central")
    r = res["S1 lock all 2027, 100% stocks"]
    unlocked = r["gift"] - r["floor"]
    crash_gift = r["floor"] + unlocked / (1 + EQUITY["central"][0]) * 0.65
    print(f"  S1 (100% stocks + promise lock): median gift {fmt(pct(r['gift'],50))} -> "
          f"~{fmt(pct(crash_gift,50))}; the promised floor ({fmt(pct(r['floor'],50))} median)"
          f" is untouched")


if __name__ == "__main__":
    main()
