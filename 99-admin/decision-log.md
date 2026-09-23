# Decision log

**Why this file exists:** Evaluation criterion 4 — "Articulation of Competition
Experience" — asks us to explain our research and decision-making process and to
"reflect meaningfully on the team's growth and response to challenges." We cannot
reconstruct that in December from memory. Log decisions **the day they are made**,
including the ones we later reverse. A reversal with a reason is *better* material
than a straight line.

**Format:** one entry per decision. Keep it short. "Considered" and "Rejected
because" matter as much as the decision itself.

---

### Template
```
## YYYY-MM-DD — <decision in one line>
**Status:** Open | Decided | Reversed (see <date>)
**Context:** what prompted this
**Options considered:** A, B, C
**Decision:** what we chose
**Reasoning:** why — in plain words
**Evidence:** link to script output, doc, or source
**Who:** who was in the room
**Revisit when:** the trigger that would make us reconsider
```

---

## 2026-09-16 — Workspace and research baseline established
**Status:** Decided
**Context:** Competition materials released 15 Sep; trading opens 28 Sep. Team
needed a shared, organised base before any strategy work.
**Decision:** Repository structure created (`00-competition/` → `99-admin/`);
all competition source documents archived, including the IPS and Trading Notes
requirement PDFs retrieved from the Box links on the deliverables page; rules,
evaluation criteria, deliverable specs and client brief written up; knowledge
base seeded (5 documents); past-winner research completed; macro snapshot taken;
core financial model built and run.
**Reasoning:** The rules are unusually specific this year (word limits, font
requirements, a frozen IPS, verified trading notes). Getting them wrong is a
screening failure, independent of quality. Better to encode them once.
**Evidence:** This repository.
**Who:** Research assistant, pre-kickoff.
**Revisit when:** N/A.

---

## 2026-09-16 — No strategy decisions taken yet (deliberate)
**Status:** Open
**Context:** Team is in the exploration phase by explicit instruction.
**Decision:** Six candidate differentiation angles documented in
`01-research/differentiation-angles.md`, each with evidence and a steelmanned
counter-argument. **None adopted.**
**Reasoning:** Committing early to a thesis before checking what WInS actually
lists, and before testing whether each angle changes a real allocation, risks
building a report around a story rather than an analysis.
**Revisit when:** After the WInS practice window (by 25 Sep) and after the team's
first working session.

---

## 2026-09-23 — No standing roles; one administrative Team Leader, everyone polyvalent
**Status:** Decided
**Context:** First full-team meeting, all four present. `06-team/` proposed five
standing roles (Team Leader, liability & fixed income, growth & research,
modelling & risk, writing & client communication), with one person doubling up.
**Options considered:**
A — five standing subject-matter roles as originally drafted;
B — two broad roles (quant / written);
C — no subject-matter roles at all: a single administrative Team Leader, all
work assigned as dated one-off tasks to named people.
**Decision:** C. The Team Leader role is retained because the rules require a
single point of contact and submitter; it carries no subject-matter ownership.
**Reasoning:** With four people, five specialisms means each of us understands
roughly a quarter of our own strategy. All members present at semifinals, and
any judge can ask any of us why the reserve is discounted at the rate it is. We
would rather all be able to answer than each be able to answer one question
well. Polyvalence also removes the single-point-of-failure risk that a
four-person team carries: if a domain has one owner and that owner is ill in
late October, the domain stops.
**Known cost, accepted:** Wharton's FAQ says teams "should assign different
roles to members", and criterion 4 rewards demonstrated teamwork. A roles table
is the easy way to evidence division of labour; we have given that up. We cover
it by writing every assignment down in `06-team/task-log.md` — named person,
date, output — so the evidence exists in a different form. Second cost: nobody
has default ownership of the unglamorous standing obligations (decision log,
reproducibility check, rules check, trading note review), so these are named
explicitly and reassigned weekly.
**Evidence:** `06-team/working-model.md`, `06-team/task-log.md`.
**Who:** All four members. Decision taken by the team leader with the team.
**Revisit when:** If, at any fortnightly criteria review, a member cannot
explain the whole case end to end — that is the failure condition for this
model and we should say so here rather than quietly drift back into silos.
Also revisit if task-log lines start going unassigned or unclosed.

---

## 2026-09-23 — Adopted Angle B: engineer the funding certainty rather than estimate it
**Status:** Decided
**Context:** First full-team working session. Six candidate angles had been
documented on 16 Sep with none adopted. The team asked for the first real
strategic fork. It was framed as: the case demands the ten payments be funded
"with a high degree of certainty" — do we satisfy that sentence with a
**structure** (cash flows that match the liability) or with a **probability**
(a diversified portfolio and a Monte Carlo score)?
**Options considered:**
A — Engineer it. Buy Treasuries maturing 2033–2042 sized to pay each $50,000
bill; the residency is then funded regardless of markets, and the remaining
capital becomes an unconstrained growth sleeve funding the facility gift.
B — Estimate it. One diversified portfolio, certainty defined statistically as
a probability threshold.
**Decision:** A. Angle B of `01-research/differentiation-angles.md` is adopted
as the governing framework.
**Reasoning:** The comparison that decided it, from
`03-modeling/src/barbell_comparison.py`:

| | Balanced whole portfolio | Defease + 100% equity sleeve |
|---|---|---|
| Funding certainty | 95.73% | 100%, by construction |
| Median facility gift | $210,350 | $206,817 |
| 5th-percentile gift | $7,677 | $120,028 |
| 2031 co-sponsor quote, worst case | effectively undefined | $119,074 |

The median facility gift is essentially unchanged. Certainty is therefore not
being bought at the expense of the thing Laura cares about — it is being bought
by giving up the top tail. The 2031 row mattered most in discussion: Laura must
quote co-sponsors a range two years before the reserve is struck, and under the
statistical approach the honest floor of that range is near zero.
**The case for it, in full.** Nine arguments, strongest first:

1. **The 2031 problem has no other solution.** Laura must quote co-sponsors a
   range in 2031 for a gift she makes in 2033. Under a statistical approach the
   honest bottom of that range is near zero, because a bad 2032 could damage
   both the gift and the reserve. She would be promising real people a number
   backed by hope. The structure is close to forced by this one constraint, and
   it is the constraint most teams will read past.
2. **Sequence-of-returns risk disappears.** A portfolio paying out $50,000 a
   year for ten years is exposed not just to *what* returns are but to *what
   order they arrive in*. Bad years early, while money is leaving, cannot be
   recovered from. Matched maturities have no sequence risk at all — the bond
   maturing in 2038 does not care what happened in 2035.
3. **It turns an unanswerable question into a checkable one.** "Is 95.7% a high
   degree of certainty?" has no defensible answer, because we chose the
   threshold ourselves. "Do these bonds mature on these dates?" can be verified
   by anyone. We would rather be checked than believed.
4. **The case hands us a perfectly hedgeable liability and it would be careless
   not to use it.** The $50,000 payments are explicitly fixed in nominal terms —
   not inflation-adjusted. That is unusual, and it means an ordinary Treasury
   matches the obligation exactly. Had the payments been inflation-linked we
   would face basis risk even with TIPS. The precision is free; declining it is
   a choice.
5. **Certainty is unusually cheap right now, which is an opportunity, not a
   retreat.** The same ladder cost $325,868 on the 2 January 2026 curve and
   $301,264 on 15 September — a $24,604 swing in eight months, because the
   10-year moved from 4.19% to 5.00%. This is not "be cautious"; it is "buy the
   thing while it is on sale." That framing fits a client described as pursuing
   unconventional opportunities with an entrepreneurial mindset.
6. **Risk is relocated, not removed.** Total portfolio risk does not fall to
   zero — it is concentrated in the growth sleeve, where a bad outcome costs
   Laura a smaller building and never a broken promise. The same dollar of
   volatility is worth more when it cannot hurt anything that matters. This is
   the answer to anyone who calls the strategy timid: we are taking *more*
   equity risk per dollar at risk, not less.
7. **It fits who the client is.** Laura is a creator, not a portfolio manager.
   Her stated philosophy — "the only person who needs to believe in something is
   yourself" — describes someone making a promise to a community she intends to
   keep personally. The structure lets her stop watching markets and go make
   books, and it means the residency opens in 2033 whatever the decade does.
8. **It survives the freeze.** Strategy locks 6 November and is evaluated
   4 December. A statistically-justified allocation can look wrong in December
   for reasons entirely outside our control. A matched ladder's central claim is
   unchanged by a month of market movement.
9. **It produces the trading discipline the rules reward.** A ladder is bought
   once and held. That leaves almost the whole 200-trade budget unused and every
   trade heavily reasoned — which is itself evidence, and cheaper at $25 a trade.

**The objections, and our answers:**

1. *We lock the 15 Sep 2026 curve forever.* True, and if yields rise further we
   will have overpaid for certainty. But this costs opportunity only; it can
   never cost the residency. We would rather explain a smaller gift than a
   broken promise.
2. *The growth sleeve has one five-year window and no recovery time.* A crash
   arriving in 2032 takes the gift to its floor. This is real, and it is exactly
   why the sleeve glidepath (Q4) is still open rather than assumed away. Note
   the floor is $120,028, not zero — the objection is about the size of the
   gift, not about whether one exists.
3. *"An appropriate balance between pursuing growth and protecting capital" — is
   67% in Treasuries balanced?* We think the sentence is asymmetric on purpose:
   she says **pursuing** growth and **protecting** capital. Protection is the
   requirement; growth is the aspiration. We have read it that way deliberately
   and should say so rather than pretend the phrase is neutral.
4. *Over-fitting (Q7).* Still live. Adopting an idea is not the same as having
   tested it, and Q7 stays open with someone assigned to attack it.

*(These arguments are ours to defend, not to quote. Any version that reaches the
IPS or Final Report must be rewritten in the team's own words.)*

**Evidence:** `03-modeling/src/barbell_comparison.py`,
`03-modeling/output/barbell_comparison_run.txt`,
`03-modeling/src/laura_core_model.py` §4.
**Who:** All four members.
**⚠️ What this decision does NOT settle:** the *calibration*. Full defeasance at
the start of 2027 versus partial defeasance with a pre-committed glidepath is a
separate decision and is not taken. See the open questions table.
**Revisit when:** The WInS instrument answer (open question #1) lands on 25 Sep.
If long-dated Treasuries and target-maturity bond ETFs are both unavailable, the
implementation weakens to a duration-matched approximation and we must say so
plainly rather than quietly restate the claim.

---

## 2026-09-23 — Proceeding on the ladder before confirming the instrument exists in WInS
**Status:** Decided
**Context:** The adopted strategy needs Treasuries maturing 2033–2042, or a
close substitute. We have not yet confirmed what WInS lists (open question #1),
and the practice window closes 25 Sep.
**Options considered:**
A — hold the strategy decision until the instrument is confirmed;
B — commit to the structure now and solve the implementation as we go, falling
back through a ranked list of substitutes.
**Decision:** B.
**Reasoning:** The structure is the idea; the instrument is the expression of
it. Waiting would have cost us the whole first week of trading for information
that changes how precisely we build the ladder, not whether we want one. The
fallback ladder is ranked in advance so the decision is not made under pressure
later:
1. Individual Treasury notes/bonds maturing 2033–2042 — exact match.
2. Treasury STRIPS (zero-coupon) — exact match, and no reinvestment of coupons.
3. Target-maturity bond ETFs (iShares iBonds, Invesco BulletShares) — close
   match; each fund holds bonds maturing in one year and then liquidates.
4. Duration-matched conventional bond ETFs — an approximation, **materially
   weaker**, and if we end up here we say so plainly in the IPS rather than
   restating the certainty claim as though nothing changed.
**⚠️ Constraint on "as we go":** the IPS freezes on 6 November. The
implementation must be settled and traded before then, not discovered
afterwards. "As we go" means the next five weeks, not the next five months.
**Who:** All four members.
**Revisit when:** 25 Sep, when the WInS instrument answer lands.

---

## Open questions awaiting resolution
*(mirrors the end of `01-research/differentiation-angles.md`)*

| # | Question | Blocking | Owner | Due |
|---|---|---|---|---|
| 1 | Which Treasury maturities does WInS list? Zeros/STRIPS? Target-maturity ETFs? | ⚠️ **Now critical** — implementation of the adopted strategy | | 25 Sep |
| 2 | Does the human-capital angle (A) change any actual allocation? Does it still earn its place alongside B? | Whether we run one angle or two | | Early Oct |
| 3 | ~~What 2033 reserve discount rate do we assume?~~ **Largely resolved by the 23 Sep decision** — the rate is the yield on the bonds we actually buy, not an assumption. Remaining question: which convention (annual effective vs bond-equivalent) the model states | IPS wording | | Before IPS |
| 4 | Glidepath — now applies to the **growth sleeve**, not the whole portfolio. Does the sleeve de-risk into 2033, and on what trigger? | Sleeve design | | Mid Oct |
| 5 | ~~Is the co-sponsor range floor structural or statistical?~~ **Resolved: structural**, by the 23 Sep decision | Final Report | | — |
| 6 | How much equity risk in the growth sleeve? Reframed by the decision: the sleeve protects nothing, so the question is Laura's tolerance for a variable *gift*, not for a funding shortfall | Sleeve design | | Early Oct |
| 7 | Are we over-fitting to the defeasance insight? | Whole strategy | | Ongoing |
| **8** | **NEW — calibration: full defeasance at 2027, or partial with a pre-committed glidepath?** Full defeasance removes six years of compounding on two-thirds of the capital | The central remaining strategy decision | | Early Oct |
| **9** | **NEW — what goes in the growth sleeve?** The adopted strategy makes this the only place individual security selection lives | Trades, Trading Notes | | Early Oct |
