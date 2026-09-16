# Competition Brief — the precise rules

*Authoritative summary. Sources: 2026 Competition Guide, Infographic, Gao Case
Study (archived in `source-documents/`), plus the official IPS and Trading Notes
Analysis requirement PDFs and the competition websites
(wghsinvcomp.smapply.us and globalyouth.wharton.upenn.edu), retrieved 16 Sep 2026.*

---

## 1. What the competition actually is

A ten-week exercise in **client-driven portfolio management**. Wharton's own
framing, verbatim:

> "This is not a competition to see which team can make the most money in a few
> weeks. Your challenge is to develop a thoughtful long-term investment strategy
> for your client and demonstrate that your investment decisions support that
> strategy."

And explicitly, we are **not** evaluated on:
- portfolio ranking
- how many trades we make
- whether we outperform other teams
- whether the portfolio makes money during the competition

The simulator portfolio is *evidence of decision-making*, nothing more.

### The five-step roadmap (from the official infographic)
1. **Understand** — the client, goals, funding needs, risk, uncertainty.
2. **Develop** — principles for growth, liquidity, funding reliability, risk,
   financial flexibility.
3. **Implement & document** — build the portfolio in WInS; write Trading Notes.
4. **Articulate** — the IPS formalises the strategy and the decision framework.
5. **Evaluate** — the Final Report assesses implementation and makes the
   recommendations.

> **Core principle, verbatim:** "Strategy guides every decision." Strong
> submissions connect the client's goals, research, portfolio decisions and
> final recommendations through *one clear and cohesive investment strategy*.

---

## 2. Scale and odds

| Cycle | Registered | Reports submitted | Semifinalists | Finalists |
|---|---|---|---|---|
| 2022–23 | 3,200 (53 countries) | 1,400 | 55 | 10 |
| 2024–25 | ~5,000 | ~1,800 | 50 | 10 |
| 2025–26 | ~6,300 | ~2,300 (79 countries) | 50 | 11 |

So: roughly **1 in 45** submitted reports reaches the semifinals, **1 in ~200**
reaches the finale. The filter is written quality, not returns.

---

## 3. Team and eligibility rules

- 4–6 students, grades 9–12, **all from the same school**. Falling below 4 or
  exceeding 6 = disqualification. We are 4 — we have **zero slack**. If one
  member leaves after the roster locks on 9 October we are at the minimum and
  another departure ends our run.
- Student **team leader must be ≥ 16 on 28 September 2026** and is the single
  point of contact and submitter. Changing the leader after 28 Sep needs approval.
- One teacher/educator advisor from our school. The advisor **may not make
  decisions for us or actively participate in trading or strategy**. A parent or
  finance professional may act as an unpaid *secondary* advisor.
- **Paid advisors, education consultants, or any camp/course claiming to teach
  this competition = automatic disqualification.**
- Roster locks 9 October. One shared WInS account for the whole team.
- **Contacting the client (Laura Gao) is grounds for disqualification.** Do not
  email her, DM her, or approach her at an event.

---

## 4. Trading rules (WInS)

| Rule | Detail |
|---|---|
| Starting cash | $300,000 virtual (separate from the case-study cash flows) |
| Trading window | 28 Sep 2026 → 6 Nov 2026, then frozen permanently |
| Max trades | **200** for the whole team, whole competition |
| Volume cap | May not trade more than 2× a security's current daily volume |
| Stocks | Any stock on WInS priced **≥ $5** (or local-currency equivalent) |
| ETFs | Any ETF available on WInS |
| Bonds | Treasury bonds of the **US, UK, Germany, France, Italy, Netherlands** |
| Prohibited | Margin, short selling, stock-secured debt, crypto, derivatives |
| Commissions | $25 per stock trade, $10 per Treasury bond trade (charged on fills only) |
| Execution | US orders fill at real-time prices during 9:30–16:00 ET; outside hours they fill at next open. International equities clear at end of the applicable trading day. Bond prices update once daily at US open; coupons pay semi-annually. |
| FX | Conversions automatic, but FX moves affect holding values |
| Corporate actions | Dividends, splits, coupons are all applied |
| Diversification | No required sector allocation or minimum sector count |

Practical notes for a team in France: we are UTC+1/+2, so the US market opens at
15:30 or 16:30 our time. Wharton explicitly says we are *not* expected to stay up
to trade; queue orders while the market is closed. The 200-trade cap and the $25
commission both push the same way — **few, deliberate, well-documented trades.**

---

## 5. The three graded deliverables

Evaluators consider all three **together** and expect a consistent strategy
across them. Full specs in `deliverable-specs.md`.

| Deliverable | Due | Purpose |
|---|---|---|
| Trading Notes Analysis | 23 Oct | Demonstrate decision-making |
| Investment Policy Statement | 6 Nov | Articulate and finalise the strategy |
| Final Report | 4 Dec | Evaluate strategy and implementation; make the recommendations |

Plus two ungraded-but-mandatory items: the **Team Roster** (9 Oct) and
**official school documentation** on letterhead (with the Final Report,
4 Dec — request it early).

**The IPS is a one-way door.** After 6 November the strategy is the official
record and may not be revised. The Final Report evaluates *that* strategy. We may
say "we would decide differently now"; we may not quietly rewrite the thesis.

---

## 6. What the client requires of the strategy

From the case study, the strategy must:
- Support the ten-year operating commitment **with a high degree of certainty**.
- Determine a **responsible facility contribution**.
- Address how investment uncertainty affects both.
- Communicate the potential facility contribution to co-sponsors **clearly and
  credibly**, as a *range* with a stated confidence level.
- Preserve **appropriate financial flexibility**.

And we must state our assumptions about: investment performance, timing of cash
flows, outside funding, the effect of inflation on projections and facility
costs, and how much flexibility Laura should keep.

**Explicitly out of scope** (do not waste words on these): estimating the
facility's total cost, a construction budget, the project's funding gap, a
business plan for the residency, the size/composition of a separate contingency
fund or endowment, personal income tax, capital-gains tax, and Taiwanese legal
or regulatory requirements.

---

## 7. AI and integrity — read this twice

Wharton's policy, which we follow literally:

- Generative AI **is permitted for brainstorming and idea generation**.
- "**AI-generated work may not be submitted as your own.**" Substantial
  completion of a task by AI is treated exactly like substantial completion by
  another person — i.e. academic dishonesty.
- **All AI-generated material must be properly cited**, like any other source,
  in the Works Cited of the Final Report. (The IPS forbids citations entirely —
  which is a further reason the IPS text must simply be ours.)
- AI output "may be inaccurate, incomplete, or otherwise problematic." We verify.
- Penn may run AI-detection tooling on submissions.

Teams must also follow **Penn's Code of Academic Integrity** and — notably —
**the CFA Institute's Asset Manager Code**. That second one is an opportunity,
not just a rule: it is a professional standard we can visibly operate by
(loyalty to the client, suitability, full disclosure, reasonable basis for
recommendations). Very few high-school teams will actually read it.

**Our working line:** a Python Monte Carlo we wrote and can explain is *our*
analysis. An LLM's summary of a 10-K is a *source* and gets cited. An LLM's
draft of our IPS is a violation. There is no grey area we need to live in.

### Other disqualifying acts
Contacting the client; offensive team names; removing members without approval;
team-size violations; paid advisors; unapproved advisor or leader changes;
plagiarism; recording or posting semifinal/finale presentations; threatening or
offensive conduct.

---

## 8. Prizes
- All eligible teams: digital credential/participation badge.
- Semifinalists & finalists: certificate of achievement.
- Top 10: waived fee for the "Understanding Your Money" course.
- Champion: free enrolment in a Wharton Global Youth summer online program, and
  the school gets fast-tracked to the following year's semifinals.
- Runners-up: 50% discount on select summer programs.

Note the finale is **not funded** — teams pay their own travel to Philadelphia,
or present by videoconference. Worth knowing now, in September, not in April.
