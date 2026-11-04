"""Gift-policy comparison, 4 Nov 2026. Run with python3 this/path.py.

Dependencies: numpy. All investment returns below are ASSUMPTIONS, not current
market data. Normalized wealth=100 starts 1 Jan 2028, after the second case
contribution and after a separately verified operating-payment allocation.
This deliberately does not reuse legacy dollar forecasts or certify that ladder.
No numerical result is a promise or a calibrated real-world probability.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import contextlib
import io
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261104  # CONVENTION: reproducible, common random paths for fair comparisons.
N = 120_000  # CONVENTION: sample size, not evidence about true probabilities.
WEIGHTS = (0.0, 0.4, 0.6, 0.8, 1.0)  # CONVENTION: policy candidates.
LOCKS = (0.5, 0.75, 0.9, 1.0)  # CONVENTION: 2031 fraction moved to backing assets.
FEE = 0.0015  # ASSUMPTION: 0.15% annual all-in fund/rebalancing drag.
COST = 0.001  # ASSUMPTION: 0.10% initial and lock execution drag.
START = 100.0  # CONVENTION: 100 units, available 1 Jan 2028 after operating funding.

@dataclass(frozen=True)
class Scenario:
    name: str
    equity_mean: float  # ASSUMPTION: annual arithmetic mean, including crash mixture.
    normal_log_sd: float  # ASSUMPTION: ordinary-year log-return dispersion.
    short_yield: float  # ASSUMPTION: rolled one-year Treasury holding-period return.
    lock_coupon: float  # ASSUMPTION: 0% cash backing; positive rates sensitivity ONLY.
    crash_prob: float = 0.05  # ASSUMPTION: independent annual crash-regime frequency.
    crash_return: float = -0.35  # ASSUMPTION: extra multiplicative crash component.

SCENARIOS = (
    Scenario('pessimistic', .03, .16, .01, .00),
    Scenario('base', .065, .14, .03, .00),
    Scenario('optimistic', .09, .14, .05, .00),
    Scenario('no-risk-premium', .03, .14, .03, .00),
)

def quantiles(x):
    return tuple(float(t) for t in np.percentile(x, (5, 50, 95)))

def simulate(s, fee=FEE):
    rng = np.random.default_rng(SEED)
    # ASSUMPTION: mixture lognormal with rare multiplicative downside shock.
    # Adjust ordinary-year mean so whole mixture has the stated arithmetic mean.
    # Still iid and uncalibrated: deterministic timing stresses supplement it.
    shocks = rng.random((N, 5)) < s.crash_prob
    normals = rng.standard_normal((N, 5))
    correction = 1 + s.crash_prob * s.crash_return
    log_mu = math.log((1+s.equity_mean)/correction)-.5*s.normal_log_sd**2
    eq = np.exp(log_mu+s.normal_log_sd*normals) * np.where(shocks, 1+s.crash_return, 1)
    result = {}
    for w in WEIGHTS:
        growth = (w*eq+(1-w)*(1+s.short_yield))*(1-fee)
        v31 = START*(1-COST)*growth[:, :3].prod(axis=1)
        for f in LOCKS:
            # ASSUMPTION: BASE=0% cash backing. Positive coupon is hypothetical
            # sensitivity only: a par two-year conventional Treasury with coupons
            # held idle. No availability of that future security is asserted.
            floor = f*v31*(1-COST)*(1+2*s.lock_coupon)
            uncommitted = (1-f)*v31*growth[:, 3:].prod(axis=1)
            total = floor+uncommitted
            result[(w,f)] = (v31, floor, total, uncommitted)
    return result

def deterministic(w, f, eq_returns, bond_return=.03, coupon=.00, fee=FEE):
    wealth = START*(1-COST)
    for er in eq_returns[:3]:
        wealth *= (w*(1+er)+(1-w)*(1+bond_return))*(1-fee)
    v31 = wealth
    floor = f*v31*(1-COST)*(1+2*coupon)
    remaining = (1-f)*v31
    for er in eq_returns[3:]:
        remaining *= (w*(1+er)+(1-w)*(1+bond_return))*(1-fee)
    return v31, floor, floor+remaining, remaining

def conditional_2031():
    """A fresh range given wealth observed in2031; not a2028 forecast."""
    floor = START * .75 * (1-COST)
    print('\nCONDITIONAL 2031 RANGE: observed Gift assets = 100 AFTER an operating-coverage recheck')
    print('Choice: 75% cash backing at 0%; 0.10% execution cost; 25 units unpromised in 40/60.')
    print(f'Backed floor = 100 x 0.75 x 0.999 = {floor:.3f}.')
    print('Two future years only. Maximum donation ceiling = floor + max(U2033 - 25, 0).')
    print('Actual donation may be between the honored floor and this ceiling after a fresh flexibility review.')
    print('The ceiling is NOT an instruction to donate the maximum, and NOT total Gift assets.')
    print('Scenario           Floor  Ceiling q90  Ceiling q95  Ceiling exactly floor  Median retained  Model coverage [floor,q90]')
    for scenario in (SCENARIOS[1], SCENARIOS[0], SCENARIOS[3]):
        v, oldfloor, total, remaining = simulate(scenario)[(.4,.75)]
        # Same common future paths as the main simulation; strip out its random
        # first-three-year wealth. These last two years are independent by assumption.
        u = 25 * remaining / ((1-.75)*v)
        ceiling = floor + np.maximum(u-25,0)
        retained = np.minimum(u,25)
        q90,q95 = np.percentile(ceiling,(90,95))
        coverage = np.mean((ceiling>=floor) & (ceiling<=q90))
        atom = np.mean(ceiling == floor)
        assert np.allclose(ceiling+retained,floor+u)
        print(f'{scenario.name:<18} {floor:6.3f} {q90:12.3f} {q95:12.3f} {atom:21.2%} {np.median(retained):16.3f} {coverage:27.2%}')
    print('These percentages describe the specified simulation, not calibrated real-world confidence.')
    print('If the floor is honored and actual gifts stay below their modeled ceilings, [floor,q90]')
    print('covers AT LEAST the modeled 90% fraction, not necessarily exactly 90%: discretion can lower extras.')
    print('Unconditional 2028 forecasts also include uncertain wealth by2031; this table conditions on100 observed then.')
    print('\nOPERATING TOP-UP BRANCH: a later operating shortfall uses unpromised assets first, then floor cash.')
    print('Arithmetic illustration only: U2033 = 20 before top-up; original floor = 74.925.')
    print('Top-up  U used  Floor used  Floor remaining  U remaining  Max donation ceiling  Old pledge shortfall')
    for topup in (0.,15.,30.):
        u_used=min(20.,topup)
        floor_used=min(floor,max(topup-20.,0))
        new_floor=floor-floor_used
        new_u=20.-u_used
        ceiling=new_floor+max(new_u-25,0)
        retained=min(new_u,25)
        shortfall=floor-new_floor
        assert abs(topup+ceiling+retained-(floor+20))<1e-8
        print(f'{topup:6.1f} {u_used:7.1f} {floor_used:11.1f} {new_floor:16.3f} {new_u:12.1f} {ceiling:21.3f} {shortfall:20.3f}')
    print('A 15-unit top-up leaves the pledge backed but reduces flexibility. A 30-unit top-up consumes')
    print('10 units of backing: the old pledge is short. No unconditional floor or 90% coverage survives that branch.')
    print('Review operating coverage before pledging and monitor it afterward; do not count one dollar twice.')

def audit():
    print('LEGACY MODEL AUDIT — do not reuse old guarantees or dollar forecasts')
    print('1. Full-scale 2027 ladder $319,892 exceeds available first contribution $300,000.')
    deficit = 319_892 - 300_000
    print(f'   Gap={319_892:,.0f}-{300_000:,.0f}=${deficit:,.0f}.')
    print('   Legacy S1 code: 2028 growth=150000+(300000-real_ladder)*(1+one_year).')
    print('   That carries negative 2027 cash at a borrowing rate; no staged holdings are modelled.')
    print('   Correct implementation must use only available cash, complete ladder in2028,')
    print('   reprice its missing portion, and retest every payment. No debt/margin assumed here.')
    print('2. Fund coverage price*(1+(yield-expense)*years) is an approximation, not contractual')
    print('   distributions plus terminal cash. Final fund payout/reinvestment risks remain;')
    print('   2% buffer has not been shown sufficient. Earlier comments also say reinvestment')
    print('   while the executed helper uses simple interest/0% idle cash.')
    print('3. Legacy simulator sets S1 funded=True by construction. 100% is conditional on its')
    print('   assumed cash schedule; not an empirically estimated operating success probability.')
    print('4. WInS two-thirds scaling compresses $450k into an initial $300k snapshot; the')
    print('   actual client has $300k in2027 and $150k only in2028. They are not same cash timeline.')
    print('5. Legacy S1 growth in2028-30 correctly gets only three annual return intervals to')
    print('   2031, but initial funding above invalidates its claimed day-one full lock.')
    print('6. Old curve/prices dated Sep/Oct2026 are not verified live4Nov quotes.')
    print('Old headline locations: 99-admin/decision-log.md, 99-admin/state.md,')
    print('02-strategy/proposal-2026-09-30.md, 06-team/briefings/2026-09-30-lock-in-the-promise.md,')
    print('03-modeling/README.md, output/thesis_decision_2026_09_30_run.txt,')
    print('00-competition/client-brief-laura-gao.md. They are not overwritten by this run.\n')

def main():
    audit()
    print('NEW POLICY MODEL: amounts per100 units actually available1Jan2028 for Gift Portfolio')
    print('Operating money excluded; no funded-operating probability or dollar gift is claimed.')
    print(f'Seed={SEED}; simulations={N:,}; annual fee={FEE:.2%}; execution={COST:.2%}.')
    print('p5/median/p95 are simulated percentiles under assumptions, not calibrated confidence.')
    print('Base floor is CASH HELD AT0% from2031to2033, after assumed execution costs.')
    print('No2033Treasury availability is assumed. Positive coupon sensitivity is hypothetical only.')
    print('Floor conditional on no withdrawals and no operating shortfall consuming that same cash.')
    print('A locked fraction is NOT the eventual gift fraction or a separate contingency reserve.')
    for s in SCENARIOS:
        result = simulate(s)
        print(f'\nSCENARIO {s.name}: equity arithmetic mean{s.equity_mean:.1%}, ordinary logSD{s.normal_log_sd:.0%},')
        print(f'short rate{s.short_yield:.1%}, 2031cash backing rate{s.lock_coupon:.1%}, extra crash{s.crash_return:.0%} chance{s.crash_prob:.0%}/yr')
        print('Equity Lock |2031wealth p5 med p95|2033backedfloor p5 med|2033total p5 med p95|Pr(floor<initial100)')
        for w in WEIGHTS:
            for f in LOCKS:
                v, floor, total, rem = result[(w,f)]
                qv, qf, qt = quantiles(v), quantiles(floor), quantiles(total)
                print(f'{w:4.0%} {f:4.0%} |'+ ' '.join(f'{x:6.1f}' for x in qv)+' |'+
                      ' '.join(f'{x:6.1f}' for x in qf[:2])+' |'+ ' '.join(f'{x:6.1f}' for x in qt)+
                      f' |{np.mean(floor<START):6.1%}')
        # Show choice tradeoffs rather than elevate no-breach by-construction to evidence.
        print('Median2033 total (60% equity,75%lock) - (0%equity,75%lock): '
              f'{np.median(result[(.6,.75)][2])-np.median(result[(0,.75)][2]):+.2f} units')
    print('\nFLEXIBILITY DISCIPLINE: promise cash floor; do not promise remaining initial capital.')
    print('At2033maximum donation ceiling=floor+max(uncommitted2033-uncommitted2031,0). Retained=min(uncommitted2033,uncommitted2031).')
    print('Actual extras are discretionary up to this ceiling; retaining more is allowed if the promised floor remains honored.')
    print('This is a spending rule within Gift assets, not a separate contingency/endowment fund.')
    print('Equity Lock |maximum donation ceiling p5 median p95|retained median|Pr(retained<uncommitted2031)')
    base=simulate(SCENARIOS[1])
    for w in WEIGHTS:
        for f in LOCKS:
            v,floor,total,rem=base[(w,f)]
            initial=(1-f)*v
            gift=floor+np.maximum(rem-initial,0)
            retained=np.minimum(rem,initial)
            assert np.allclose(gift+retained,total)
            print(f'{w:4.0%} {f:4.0%} |'+' '.join(f'{x:6.1f}' for x in quantiles(gift))+
                  f' |{np.median(retained):6.1f} |{np.mean(retained<initial):6.1%}')
    print('\nDETERMINISTIC TIMING STRESSES;75%lock; eq[2028,2029,2030,2031,2032]')
    paths = {
        'steady6.5%': (.065,)*5,
        'crash2030-beforepromise': (.065,.065,-.40,.065,.065),
        'crash2032-afterpromise': (.065,.065,.065,.065,-.40),
        'bad2028and2030': (-.30,.065,-.30,.065,.065),
        'zeroequityreturn': (0,)*5,
    }
    print('Path Equity |2031wealth |2033backed |2033total |uncommitted |maxdonationceiling |retained')
    for name, path in paths.items():
        for w in WEIGHTS:
            v, floor, total, rem = deterministic(w,.75,path)
            gift=floor+max(rem-.25*v,0)
            retained=min(rem,.25*v)
            print(f'{name:<26} {w:4.0%} |{v:9.2f} |{floor:10.2f} |{total:9.2f} |{rem:11.2f} |{gift:13.2f} |{retained:8.2f}')
    print('\nSENSITIVITIES for60%equity/75%lock; other base assumptions unchanged')
    for fee in (0,.0015,.005):
        r=simulate(SCENARIOS[1],fee)[(.6,.75)]
        print(f'Annual fee{fee:.2%}:2033total p5/median/p95='+ '/'.join(f'{x:.2f}' for x in quantiles(r[2])))
    for coupon in (0,.01,.03,.05):
        s=Scenario(f'coupon{coupon}',.065,.14,.03,coupon)
        r=simulate(s)[(.6,.75)]
        print(f'2031lock coupon{coupon:.1%}:floor median{np.median(r[1]):.2f},totalmedian{np.median(r[2]):.2f}')
    conditional_2031()
    print('\nSTAGED2027/2028 BUDGET FEASIBILITY EXAMPLE, NOT AN AUDITED HOLDINGS SCHEDULE')
    print('Using legacy dated319892cost only as a budget illustration:2027contribution300000,')
    print('unfunded portion19892;2028contribution150000 first buys the missing protection.')
    for factor in (.7,1.,1.3,2.):
        gap=(319_892-300_000)*factor
        print(f'Missingprotection price factor{factor:.1f}:2028topup={gap:,.2f};leftforGift={150_000-gap:,.2f}.')
    print('This does not validate buying300000ofparticularholdings in2027; exact datedcash flows')
    print('and prices must be rebuilt. Highercosts first reduce growthcapital, never create debt.')
    print('\nHAND CHECK:2031observedGift100;75%cashlock;0%cashyield;execution0.10%')
    floor=START*.75*(1-COST)
    initial=25.
    remainder=initial*(.4*.60+.6*1.03)*(1-FEE)
    donation=floor+max(remainder-initial,0)
    retained=min(remainder,initial)
    print(f'Cashfloor=100x0.75x0.999={floor:.3f};25remainunpromised.')
    print(f'Inonebadyear(-40%equity,+3%Treasury),40%equityremainder=25x(0.40x0.60+0.60x1.03)x0.9985={remainder:.6f}.')
    print(f'Donation={floor:.3f}+max({remainder:.6f}-25,0)={donation:.3f};retained={retained:.6f}.')
    print('Thepledgedfloorstaysbacked;unpromisedcapitalcanfall. Itisnotaguaranteedflexibilityamount.')
    print('\nBEGINNER EXAMPLES: same observed 2031 Gift balance and net cash backing')
    for residual in (28.0, 20.0):
        extra = max(residual - initial, 0.0)
        ceiling = floor + extra
        print(f'If 25 unpromised units become {residual:.0f}, extra-gift ceiling = '
              f'max({residual:.0f} - 25, 0) = {extra:.0f}; '
              f'total-gift ceiling = {floor:.3f} + {extra:.0f} = {ceiling:.3f}.')
        assert math.isclose(ceiling + min(residual, initial), floor + residual)
    print('\nDECISION SUPPORTED: early protection of the operating promise remains a sound objective,')
    print('but legacy modelling does NOT prove full2027lock or100%certainty. Audit/stage funding first.')
    print('For Gift policy, diversified40%-60%equity and a2031cash-backing rule trade upside for a steadier')
    print('sponsor contribution.40%equity/75%cashlock better prioritizes downside than60%equity, with modest')
    print('base median upside sacrificed. This is a defensible POLICY CHOICE, not a numerical optimum.')
    print('0%equity wins downside;100%equity wins high-return upside; no weight dominates all scenarios.')
    print('A2030crash lowers the floor she can responsibly announce; locking in2031cannot repair that.')
    print('75%cashlock materially limits post-promise downside while leaving25%capital uncommitted;90%or100%')
    print('raises backing but reduces flexibility. Actual communicated minimum must also reserve any')
    print('needed operating top-up and flexibility BEFORE making the promise; cannot pledge same money twice.')
    print('Do not infer an exact lockfraction from a desired confidence level: locked cash and model range')
    print('answer different questions. Re-evaluate cost, missing payment coverage and true2031wealth then.')
    print('LIMITS: not calibrated historical bootstrap; iid mixture; constant short-rate scenarios;')
    print('no inflation purchasing-power forecast or localTaiwan costs; no simulator availability test.')
    print('Annual2031rebalancing assumed before lock; floor is nominalcash; no marginal taxes (outofscope).')

if __name__ == '__main__':
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    output=buf.getvalue()
    target=ROOT/'03-modeling/output/strategy_policy_2026_11_04_run.txt'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(output)
    print(output,end='')
