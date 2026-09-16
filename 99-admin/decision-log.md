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

## Open questions awaiting resolution
*(mirrors the end of `01-research/differentiation-angles.md`)*

| # | Question | Blocking | Owner | Due |
|---|---|---|---|---|
| 1 | Which Treasury maturities does WInS list? Zeros/STRIPS? Target-maturity ETFs? | Angle B feasibility | | 25 Sep |
| 2 | Does the human-capital angle change any actual allocation? | Angle A adoption | | Early Oct |
| 3 | What 2033 reserve discount rate do we assume, and how sensitive is the answer? | Reserve sizing | | Before IPS |
| 4 | Glidepath: time-based or funded-ratio-based? | IPS wording | | Before IPS |
| 5 | Is the co-sponsor range floor structural or statistical? | Final Report | | Nov |
| 6 | How much equity risk is consistent with Laura's stated risk appetite? | Whole strategy | | Early Oct |
| 7 | Are we over-fitting to the defeasance insight? | Whole strategy | | Ongoing |
