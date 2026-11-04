"""Cash-feasible operating-policy audit, 4 Nov 2026.
Run: python3 03-modeling/src/operating_audit_2026_11_04.py
Dependencies: numpy, scipy. Self-contained; no network/current quote requests.
Dated reference clean prices: recorded WInS quotes 21 Oct 2026, in
ladder_reprice_2026_10_21.py. Quantities/cash: trade-log.md 21 Oct fills.
They are scenario anchors, NOT verified 2027/28 prices or current balances.
Future prices and fund proceeds below are ASSUMPTIONS, not promises.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from collections import defaultdict
import contextlib
import io
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

ROOT=Path(__file__).resolve().parents[2]
PAY_YEARS=tuple(range(2033,2043)) # CASE FACT: Jan1 payments.
PAYMENT=50_000. # CASE FACT
CUSHION=.02 # POLICY CHOICE: tested target51k, not empirically calibrated safety.
STAGES=(date(2027,1,1),date(2028,1,1)) # CASE FACT
BUDGETS=(300_000.,150_000.) # CASE FACT; no borrowed/future cash.
# ASSUMPTION: reference clean prices unchanged in2027, shock multiplier in2028;
# accrued coupon interest recalculated for exact purchase date at0reinvestment.
# ASSUMPTION: fund aggregate net cash=referenceprice*(1-haircut), no earlier
# distribution/return credit; counted only15Dec of termination year. Deliberately
# conservative proxy, not verified underlying holdings or an issuer guarantee.

@dataclass(frozen=True)
class Asset:
    name:str
    kind:str
    ref:float
    coupon:float=0
    mat:date|None=None
    actual:int=0

ASSETS=(
 Asset('Treasury 4.750% Feb2037','bond',97.402,.0475,date(2037,2,15),29),
 Asset('Treasury 4.500% May2038','bond',94.520,.045,date(2038,5,15),30),
 Asset('Treasury 4.375% Nov2039','bond',91.555,.04375,date(2039,11,15),31),
 Asset('Treasury 4.250% Nov2040','bond',89.389,.0425,date(2040,11,15),32),
 Asset('Treasury 3.125% Nov2041','bond',76.562,.03125,date(2041,11,15),33),
 Asset('IBTO closes Dec2033','fund',23.17,mat=date(2033,12,15),actual=744),
 Asset('IBTP closes Dec2034','fund',24.28,mat=date(2034,12,15),actual=735),
 Asset('IBTQ closes Dec2035','fund',23.89,mat=date(2035,12,15),actual=1583),
 Asset('Cash held at0%','cash',1.),
)
M=len(ASSETS)

def prev_half(d):
    m=d.month-6
    return date(d.year-(m<=0),m+12 if m<=0 else m,d.day)

def coupon_dates(a):
    d=a.mat
    out=[]
    while d.year>=2026:
        out.append(d)
        d=prev_half(d)
    return sorted(out)

def cost(a,start,shock):
    if a.kind=='cash': return 1.
    if a.kind=='fund': return a.ref*(1+shock)
    dates=coupon_dates(a)
    after=min(d for d in dates if d>start)
    before=prev_half(after)
    accrued=1000*a.coupon/2*(start-before).days/(after-before).days
    return a.ref*10*(1+shock)+accrued

def commission(a):
    return 10. if a.kind=='bond' else 25. if a.kind=='fund' else 0.

def cash_events(a,start,haircut):
    if a.kind=='cash': return [(start,1.)]
    if a.kind=='fund': return [(a.mat,a.ref*(1-haircut))]
    return [(d,1000*a.coupon/2+(1000 if d==a.mat else 0))
            for d in coupon_dates(a) if d>start]

def flow_vector(a,start,haircut):
    return np.array([sum(v for d,v in cash_events(a,start,haircut)
                         if d<date(y,1,1)) for y in PAY_YEARS])

def solve(haircut,shock,fixed_first=None,first_shock=0.):
    # Integer quantities for every bond/share; cash rounded to whole dollars.
    # Separate binary trade flags charge commissions exactly once per holding/stage.
    nv=4*M
    c=np.zeros(nv)
    upper=np.ones(nv)
    lower=np.zeros(nv)
    for s,start in enumerate(STAGES):
        for j,a in enumerate(ASSETS):
            i=s*M+j
            c[i]=cost(a,start,shock if s else first_shock)
            c[2*M+i]=commission(a)
            upper[i]=450000 if a.kind=='cash' else 50000 if a.kind=='fund' else 500
    if fixed_first is not None:
        for j,q in enumerate(fixed_first):
            lower[j]=upper[j]=q
            lower[2*M+j]=upper[2*M+j]=float(q>0)
    rows=[];lo=[];hi=[]
    for s in range(2):
        row=np.zeros(nv)
        row[s*M:(s+1)*M]=c[s*M:(s+1)*M]
        row[2*M+s*M:2*M+(s+1)*M]=c[2*M+s*M:2*M+(s+1)*M]
        rows.append(row);lo.append(-np.inf);hi.append(BUDGETS[s])
    for yindex,y in enumerate(PAY_YEARS):
        row=np.zeros(nv)
        for s,start in enumerate(STAGES):
            for j,a in enumerate(ASSETS):
                row[s*M+j]=flow_vector(a,start,haircut)[yindex]
        rows.append(row);lo.append(PAYMENT*(1+CUSHION)*(yindex+1));hi.append(np.inf)
    for i in range(2*M):
        row=np.zeros(nv);row[i]=1.;row[2*M+i]=-upper[i]
        rows.append(row);lo.append(-np.inf);hi.append(0)
    res=milp(c,integrality=np.ones(nv),bounds=Bounds(lower,upper),
             constraints=LinearConstraint(np.array(rows),lo,hi),
             options={'time_limit':25,'mip_rel_gap':.00001})
    if res.x is None:
        return None,str(res.message)
    q=np.rint(res.x[:2*M]).reshape(2,M).astype(int)
    spend=[]
    for s,start in enumerate(STAGES):
        spend.append(sum(q[s,j]*cost(a,start,shock if s else first_shock)+
                         commission(a)*(q[s,j]>0) for j,a in enumerate(ASSETS)))
    assert all(x<=b+1e-4 for x,b in zip(spend,BUDGETS))
    flows=sum(q[s,j]*flow_vector(a,start,haircut)
              for s,start in enumerate(STAGES) for j,a in enumerate(ASSETS))
    surplus=flows-PAYMENT*np.arange(1,11)
    assert min(surplus)>=-1e-3
    return dict(q=q,spend=spend,surplus=surplus,flows=flows,
                gift=sum(BUDGETS)-sum(spend),optimal=bool(res.success),
                gap=getattr(res,'mip_gap',None)),str(res.message)

def print_payments(r):
    last=0.
    print('Payment date | Cash received since prior bill | Bill | Cash remaining after bill')
    for y,cumulative,surplus in zip(PAY_YEARS,r['flows'],r['surplus']):
        print(f'1 Jan {y}   {cumulative-last:>17,.2f}                50,000 {surplus:>18,.2f}')
        last=cumulative

def main():
    print('OPERATING AUDIT — dated research scenarios, NOT orders or a live portfolio certification')
    print('Case cash:300,000 on1Jan2027;150,000 on1Jan2028;ten50,000 bills Jan2033-2042.')
    print('No borrowing, coupon reinvestment, stock rescues, outside money or early use of150,000.')
    print('Reference clean prices21Oct2026; future Jan2027sameclean assumption; Jan2028shock shown.')
    print('Accrued interest recomputed at eachJan1. Purchases settle before subsequent coupons.')
    print('All bond receipts and held cash earn0%; no fund return/distribution credited beforeclosing.')
    print('Fund terminal netcash per share=recordedreferenceprice times90/95/100%; NOT a guarantee.')
    print('Model target=51,000 annual available cash (50,000 obligation+chosen2%cushion).')
    print('MILP chooses whole bonds/shares/cashdollars, stages and exact trade commissions.')
    print('Base design is robust to10%fundproceedshaircut AND30%higher2028cleanpurchaseprices.')
    design,msg=solve(.10,.30)
    if design is None:
        print('INFEASIBLE ROBUST DESIGN:',msg);return
    print('\nFEASIBLE STAGED RESEARCH EXAMPLE; solve status:',msg)
    print('Asset                                    2027 units    2028 units')
    for j,a in enumerate(ASSETS):
        print(f'{a.name:<40}{design["q"][0,j]:>11,}{design["q"][1,j]:>14,}')
    print('Bond units=$1,000face;fundunits=shares;cashunits=$1. Research quantities only.')
    for s,spent in enumerate(design['spend']):
        print(f'{STAGES[s]} contribution{BUDGETS[s]:,.2f};spent{spent:,.2f};unspent{BUDGETS[s]-spent:,.2f}.')
    print(f'Gift capital available after completion={design["gift"]:,.2f}; no assumed investmentgain.')
    print_payments(design)
    print('\nFROZEN2027 HOLDINGS; reoptimize completion only after2028prices observed')
    print('Haircut Shock |2027spend |2028spend |Giftcapital |Minimumafter-billcash |Status')
    for haircut in (0.,.05,.10):
        for shock in (0.,.10,.30,.50):
            r,status=solve(haircut,shock,design['q'][0])
            if r is None:
                print(f'{haircut:4.0%} {shock:4.0%} INFEASIBLE: {status}')
                continue
            print(f'{haircut:4.0%} {shock:4.0%} |{r["spend"][0]:10,.2f} |{r["spend"][1]:10,.2f} |{r["gift"]:10,.2f} |{min(r["surplus"]):20,.2f} |feasible')
            print_payments(r)
    print('No2028bond/fundpurchase occurs in this selected design, so2028marked-assetprice shocks')
    print('are immaterial for it. This is a cash-bridge result, not proof about futuremarketprices.')
    print('\n2027REFERENCEPRICE SENSITIVITY: reoptimize both stages, maintain separate300k/150kbudgets')
    for first_shock in (.10,.20,.30,.50):
        r,status=solve(.10,.30,first_shock=first_shock)
        if r is None:
            print(f'2027cleanprices+{first_shock:.0%}: INFEASIBLE undertheseinputs; {status}')
        else:
            print(f'2027cleanprices+{first_shock:.0%}: stage1={r["spend"][0]:,.2f};stage2={r["spend"][1]:,.2f};Gift={r["gift"]:,.2f};minafterbill={min(r["surplus"]):,.2f}.')
    print('\nCURRENT RECORDED8-HOLDING SNAPSHOT DIAGNOSTIC, separate from real stagedcase')
    print('Starting cash85,781.79 recorded21Oct2026, NOT verified4Nov. Scaledbill=50,000x2/3.')
    snapshot_start=date(2026,10,21)
    scaled=PAYMENT*2/3
    for haircut in (0.,.05,.10):
        flows=sum(a.actual*flow_vector(a,snapshot_start,haircut) for a in ASSETS)
        raw=flows-scaled*np.arange(1,11)
        topup=max(0.,float(np.max(scaled*(1+CUSHION)*np.arange(1,11)-flows)))
        remaining=85781.79-topup
        print(f'\nFund haircut{haircut:.0%}: additionalcash earmark for2%cushion={topup:,.2f};')
        print(f'85,781.79 minus earmark leaves{remaining:,.2f}potentialGiftcash (dateddiagnostic).')
        print('Year | Surplus WITHOUT earmark | Surplus WITH earmark after scaled33,333.33bill')
        for y,x in zip(PAY_YEARS,raw):
            print(f'{y} {x:>19,.2f} {x+topup:>28,.2f}')
        assert min(raw+topup)>=-1e-5
    print('\nKNOWN TREASURY CASH EVENTS FOR CHOSEN STAGED EXAMPLE (unit coupons and principal)')
    for s,start in enumerate(STAGES):
        for j,a in enumerate(ASSETS):
            n=design['q'][s,j]
            if a.kind=='bond' and n:
                print(f'{start}: {n} x {a.name}; paid{n*cost(a,start,.30 if s else 0):,.2f} beforecommission')
                for d,value in cash_events(a,start,.10):
                    print(f'  {d}: {n} x {value:.3f} = {n*value:,.2f}')
    print('\nHAND CHECK:2037Treasury pays4.75% of1,000=$47.50/year;halfyearcoupon=$23.75.')
    print('A Jan2027purchase receives Feb/Aug2027throughFeb2037;at maturity1,000principal joinscoupon.')
    print('Every receipt is held as0%cash and counted only for bills afteritsactualpaymentdate.')
    print('\nDECISION: IPS staged operating-first framework is NOT inherently unfundable in these dated')
    print('scenarios: an explicit cash-feasible schedule exists without debt or equity returns.')
    print('Conservative assumptions make cash dominate Treasuryfunds for the early maturitygap;')
    print('the robust replacement example may use nofunds. This is NOT a trade recommendation.')
    print('Do not call all85,781.79recordedcash verifiedGiftmoney: first earmark operatingrepair.')
    print('No new IPS allocation policy is required by this feasibility result; maintain staging,')
    print('cash-date checks, scenario testing and prior operating topups. Exact orders need currentquotes,')
    print('positionverification, revisedfundcashflows and rulesreview before human entry.')
    print('LIMITS: selected datedinputprice scenario, futurecleanprice assumptions, no jointlyrandomrates,')
    print('no calibrated confidencelevel, fundproceeds not verified,2%chosen not statisticallyvalidated;')
    print('cash held untilyearsaway has purchasingpower risk though obligation dollarsarefixed.')
    print('No claim that futureholdingsorprices canbe lockedtoday; no automatic liquidatingofexistingfunds.')

if __name__=='__main__':
    b=io.StringIO()
    with contextlib.redirect_stdout(b):main()
    result=b.getvalue()
    target=ROOT/'03-modeling/output/operating_audit_2026_11_04_run.txt'
    target.write_text(result)
    print(result,end='')
