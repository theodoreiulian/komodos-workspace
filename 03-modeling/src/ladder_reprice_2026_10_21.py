"""
Ladder re-price, 21 Oct 2026: the Promise Portfolio order list at today's WInS prices.

Nothing was traded on 2 Oct (WInS: 0/200 trades on 21 Oct). Before the first orders,
this re-runs the 30 Sep ladder (thesis_decision_2026_09_30.py, PART 2) with the prices
WInS shows today, and tests one change: whether to keep the 4.500% 15-Feb-2036 bond,
which WInS prices far above its neighbours.

Run:  python3 03-modeling/src/ladder_reprice_2026_10_21.py

INPUT LABELS
  MARKET DATA  - a price or yield on a stated date, with source
  CONVENTION   - a choice we made
  ASSUMPTION   - a guess
"""
from __future__ import annotations
from datetime import date

import numpy as np

import thesis_decision_2026_09_30 as base

TODAY = date(2026, 10, 21)   # CONVENTION: orders fill at the 21 Oct US open
base.TODAY = TODAY

# MARKET DATA: WInS (StockTrak) quotes read 21 Oct 2026. Funds: last price, close of
# 20 Oct. Bonds: "last price" per $1,000 face and accrued interest, "as of 06:21 AM ET".
# ASSUMPTION: fund yields = iShares 28 Sep figures less 0.11 points. Each fund's price is
# up ~0.7% since 28 Sep; divided by its ~6.5-7.5-year duration that is ~0.1 point lower
# yield, the same move WInS shows for the 2037-41 bonds.
base.IBONDS = {
    2033: ("IBTM", 21.89, 0.0511 - 0.0011),
    2034: ("IBTO", 23.17, 0.0514 - 0.0011),
    2035: ("IBTP", 24.28, 0.0519 - 0.0011),
    2036: ("IBTQ", 23.89, 0.0522 - 0.0011),
}
base.TBONDS = {
    2037: ("T-BOND 4.500% 15-Feb-2036", 0.04500, date(2036, 2, 15), 103.164, 0.801),
    2038: ("T-BOND 4.750% 15-Feb-2037", 0.04750, date(2037, 2, 15), 97.402, 0.846),
    2039: ("T-BOND 4.500% 15-May-2038", 0.04500, date(2038, 5, 15), 94.520, 0.801),
    2040: ("T-BOND 4.375% 15-Nov-2039", 0.04375, date(2039, 11, 15), 91.555, 1.870),
    2041: ("T-BOND 4.250% 15-Nov-2040", 0.04250, date(2040, 11, 15), 89.389, 1.828),
    2042: ("T-BOND 3.125% 15-Nov-2041", 0.03125, date(2041, 11, 15), 76.562, 1.344),
}
# MARKET DATA: yield implied by each WInS clean price (semi-annual, settle 22 Oct),
# computed with ytm() below. Neighbours of the 2036 bond: 2037 5.19%, 2038 5.37%.

SCALE_PAYMENT = base.PAYMENT * base.SCALE_WINS   # $33,333


def ytm(c: float, mat: date, px: float, settle: date = date(2026, 10, 22)) -> float:
    dates, d = [], mat
    while d > settle:
        dates.append(d)
        m = d.month - 6
        d = date(d.year - (1 if m <= 0 else 0), m + 12 if m <= 0 else m, d.day)
    def pv(y):
        return sum((c * 50 + (100 if x == mat else 0)) / (1 + y / 2) ** (2 * (x - settle).days / 365.25)
                   for x in dates)
    lo, hi = 0.0, 0.2
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if pv(mid) > px else (lo, mid)
    return mid


def ladder(drop_2036: bool) -> dict:
    """Same LP as 30 Sep. If drop_2036, the 2036 bond is removed and the 1 Jan 2037
    bill is paid by whatever is cheapest (in practice: extra IBTQ shares, paid out
    Dec 2035 and held as cash at 0% for ~12 months)."""
    saved = base.TBONDS.pop(2037) if drop_2036 else None
    try:
        if drop_2036:
            # the 70%-own-instrument rule cannot apply to a year with no instrument;
            # keep it for every other year by temporarily swapping the helper's keys
            orig = base.build_ladder
            lw = _build_without_2037_own(orig)
        else:
            lw = base.build_ladder(SCALE_PAYMENT, base.OWN_SHARE, TODAY, base.BUFFER)
    finally:
        if saved:
            base.TBONDS[2037] = saved
    return lw


def _build_without_2037_own(orig):
    """build_ladder with the own-instrument rule applied to every year that has one."""
    from scipy.optimize import linprog
    keys = [("T", y) for y in base.TBONDS] + [("I", y) for y in base.IBONDS]
    unit_cover, unit_cost = [], []
    for kind, y in keys:
        if kind == "T":
            cv = base._cover({y: 1000}, {}, TODAY)
            unit_cost.append(10 * (base.TBONDS[y][3] + base.TBONDS[y][4]))
        else:
            cv = base._cover({}, {y: 1}, TODAY)
            unit_cost.append(base.IBONDS[y][1])
        unit_cover.append([cv[yy] for yy in base.PAY_YEARS])
    unit_cover = np.array(unit_cover)
    cum = np.cumsum(unit_cover, axis=1)
    need = np.cumsum([SCALE_PAYMENT * (1 + base.BUFFER)] * len(base.PAY_YEARS))
    A, b = -cum.T, -need
    rows = []
    for i, (kind, y) in enumerate(keys):
        if y >= 2034:
            r = np.zeros(len(keys))
            r[i] = -unit_cover[i][base.PAY_YEARS.index(y)]
            rows.append(r)
    A = np.vstack([A, np.array(rows)])
    b = np.concatenate([b, -base.OWN_SHARE * SCALE_PAYMENT * np.ones(len(rows))])
    res = linprog(c=unit_cost, A_ub=A, b_ub=b, bounds=[(0, None)] * len(keys), method="highs")
    assert res.success, res.message
    qty = np.ceil(res.x - 1e-9)
    faces = {y: int(q) * 1000 for (k, y), q in zip(keys, qty) if k == "T"}
    shares = {y: int(q) for (k, y), q in zip(keys, qty) if k == "I"}
    cover = base._cover(faces, shares, TODAY)
    carry, surplus = 0.0, {}
    for y in base.PAY_YEARS:
        carry += cover[y] - SCALE_PAYMENT
        surplus[y] = carry
    assert min(surplus.values()) > -1, "rounded ladder is short"
    cost_t = sum(f / 100 * (base.TBONDS[y][3] + base.TBONDS[y][4]) for y, f in faces.items())
    cost_i = sum(n * base.IBONDS[y][1] for y, n in shares.items())
    nb = sum(1 for f in faces.values() if f)
    ne = sum(1 for n in shares.values() if n)
    comm = base.COMMISSION_BOND * nb + base.COMMISSION_ETF * ne
    return {"faces": faces, "shares": shares, "cost_t": cost_t, "cost_i": cost_i, "comm": comm,
            "total": cost_t + cost_i + comm, "surplus": surplus, "trades": nb + ne, "cover": cover}


def show(title: str, lw: dict) -> None:
    print("\n" + title)
    print(f"  {'Pays 1 Jan':<12}{'Instrument':<30}{'Quantity':>16}{'Est. cost':>12}")
    for y in base.PAY_YEARS:
        if lw["shares"].get(y):
            tic, px, _ = base.IBONDS[y]
            n = lw["shares"][y]
            print(f"  {y:<12}{tic:<30}{n:>9,} shares{base.fmt(n * px):>12}")
        elif lw["faces"].get(y):
            name, _, _, bp, ai = base.TBONDS[y]
            f = lw["faces"][y]
            print(f"  {y:<12}{name:<30}{f // 1000:>10} units{base.fmt(f / 100 * (bp + ai)):>12}")
        else:
            print(f"  {y:<12}{'(no own instrument)':<30}")
    print(f"  Commissions ({lw['trades']} trades){'':<38}{base.fmt(lw['comm']):>12}")
    print(f"  TOTAL{'':<59}{base.fmt(lw['total']):>12}")
    print(f"  Cash left of $300,000{'':<43}{base.fmt(300_000 - lw['total']):>12}")
    print("  Running surplus after each $33,333 bill: "
          + ", ".join(f"{y}: {base.fmt(s)}" for y, s in lw["surplus"].items()))


def main() -> None:
    print("=" * 78)
    print("Yield implied by WInS price (21 Oct 2026)")
    for y, (name, c, mat, px, _) in base.TBONDS.items():
        print(f"  {name:<30} price {px:7.3f}  yield {ytm(c, mat, px) * 100:5.2f}%")
    keep = ladder(drop_2036=False)
    drop = ladder(drop_2036=True)
    show("A  30 Sep design at today's prices (keeps the Feb-2036 bond)", keep)
    show("B  Drop the Feb-2036 bond; 1 Jan 2037 bill paid from IBTQ held one extra year", drop)
    print(f"\n  B saves {base.fmt(keep['total'] - drop['total'])} vs A and uses "
          f"{keep['trades'] - drop['trades']} fewer trade(s).")


if __name__ == "__main__":
    main()
