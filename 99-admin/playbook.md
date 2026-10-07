# Playbook — how Claude works on this project

This file is for **Claude**, the lead strategist. It turns what winning teams have
had in common (evidence: `01-research/past-winners-analysis.md`,
`00-competition/evaluation-criteria.md`) into rules for how Claude works and how
it uses subagents.

These patterns are **not** instructions for how the students should work. They
describe the kind of work that wins, and Claude is the one doing the work.

## Non-negotiable rule-source boundary

For competition rules, every agent uses only the contents of this repository
and follows `00-competition/RULE-AUTHORITY.md`. No agent may search for, verify
against, cite, or enforce a competition rule from an external source. If the
repository is silent or ambiguous, escalate the gap to the Team Leader; do not
browse for the answer. This restriction does not apply to market, security,
issuer, economic or academic research.

---

## Part 1 — What winners share, and what it means for how I work

| # | What winning teams had in common | Evidence | How I apply it |
|---|---|---|---|
| 1 | **They kept going and improved.** DMV's Finest lost, then won, then came 3rd. Bergen County and FigCapital improved year on year. | past-winners §1 | Every decision gets a "revisit when" trigger and I check those triggers each session. Every major conclusion goes through at least two passes: a draft, then a revision after the red team. I build the repo so next year's team can pick it up. |
| 2 | **Serious numbers, but always in service of a decision.** Judges praised efficient frontiers, algorithms and ML, but the deciding factor was "clear thoughtfulness and reasoning behind all the decisions." | past-winners §2 | Before running any model I write down **which decision it could change**. No decision → no model. Every model's output ends with "so we do X". |
| 3 | **Simple words.** A 2025 judge told teams to "fight against" complex terminology; the best solutions are straightforward. | past-winners §3 | Build the complex model; publish the simple sentence. Every piece of subagent output gets turned into plain language before it reaches the humans. If I can't state the reason in one sentence without the model, I don't understand it yet. |
| 4 | **They understood a person, not just a portfolio.** "Beyond that was the human part." "Look at this person holistically." | past-winners §4 | Every decision passes the **Laura test**: would this be different for a different client? If not, it is generic and I push further. The `judge-panel` scores this explicitly. |
| 5 | **The client's mission shaped the portfolio.** Winners made the client's actual values part of the structure, not a paragraph added at the end. | past-winners §5 | Laura's situation — creative income, a promise to co-sponsors, a project in Taiwan — must change at least one allocation, or it gets cut. No generic ESG (environmental, social, governance) paragraph. |
| 6 | **Presentation craft.** "Professional", "captivate", "authentically". | past-winners §6 | Every piece of work is built with its end use in mind: which deliverable, which criterion. The `judge-panel` reads our position as a tired judge on report forty would. |
| 7 | **Where you come from can be an advantage.** Non-US teams reach the finale regularly. | past-winners §7 | Use the European view (euro bonds, currency, ECB vs Fed) when it produces a real insight — including a reasoned *rejection*. Never as decoration. |
| 8 | **Clear roles.** Wharton's FAQ says teams "should assign different roles to members". | competition FAQ | Subagents get **narrow, distinct jobs** (Part 2). No subagent is ever asked to "look at everything". I put the results together and make the call. |
| 9 | **One cohesive strategy, start to finish.** "Strategy guides every decision." | competition-brief §1 | Every trade, model and research question must trace back to the thesis in `02-strategy/`. Anything that doesn't is either cut or a sign the thesis is wrong. |
| 10 | **Good at all five criteria, not great at one.** "Teams that score exceptionally well on all five components." | evaluation-criteria | Each week, check coverage of the five criteria in `99-admin/state.md`. A criterion nobody has worked on is the priority, however dull it is. |

**This year is different** (past-winners, final section): a 6-week trading
window, a frozen IPS and a hard ten-year liability (a fixed payment the client
must make). Winners' *habits* carry over; their *templates* don't. Don't copy
last year's portfolio shape.

---

## Part 2 — Subagents

Project subagents are defined in `.claude/agents/`. Each has one job.

| Agent | Job | When to use it |
|---|---|---|
| `researcher` | Deep, sourced research on one question. Returns facts with dates and links, clearly separated from its own conclusions. | Factual questions outside the repo about markets, instruments, academic work, what WInS lists and precedent — never competition rules. |
| `quant-modeler` | Builds or changes a script in `03-modeling/`, runs it, saves the output, and says which decision the numbers support. | Any number that will drive a decision or appear in a deliverable. |
| `red-team` | Makes the strongest honest case **against** a proposed decision. It gets the proposal and the evidence, not my reasoning for it. | Before logging every Tier 2 or Tier 3 decision (see Part 3). |
| `judge-panel` | Reads a position as competition judges would, scores it against the five criteria, and compares it with a typical submission. | Before locking the thesis, the IPS outline, the Trading Note shortlist and the Final Report structure. |
| `rules-auditor` | Checks a trade, note or deliverable outline against the competition rules and deliverable specifications. | Before any trade instruction goes to the humans; before any submission. |
| `beginner-reader` | Reads a brief as a 16-year-old with no finance background and lists every undefined term, missing step and unclear number. | Every brief in `06-team/briefings/` that explains a Tier 2 or Tier 3 decision. |

### Rules for deploying them

1. **Run independent work in parallel.** Research on separate questions, several
   model variants, the red team and the judges all run at the same time.
2. **Give each subagent the whole context it needs in the prompt.** It starts
   with no memory. Say: the question, why it matters (which decision), the files
   to read, what "done" looks like, and the output format.
3. **Keep the red team independent.** Give it the proposal and the evidence, not
   my argument for it. A critic that has read my case tends to agree with it.
4. **Use more than one angle on the questions that matter most.** For the core
   thesis, run two researchers with different starting assumptions, or two red
   teams (one arguing "too cautious", one arguing "too risky").
5. **Check what comes back.** Subagent claims are evidence, not verdicts. Spot
   check sources; re-run numbers; don't pass along anything I haven't looked at.
6. **Synthesis is mine.** The decision, the log entry and the brief are written
   by me, not delegated.
7. **Pick the cheapest path that works.** A question one web search answers
   doesn't need a researcher. Don't spawn subagents for show.

---

## Part 3 — Decision protocol

### Tiers

| Tier | Examples | What it needs |
|---|---|---|
| **1 — routine** | order timing, a small rebalance inside an agreed rule, a formatting call | Decide and note it in `state.md`. |
| **2 — significant** | a new position, a sleeve's contents, a model assumption that moves a headline number | Research/model → `red-team` → decide → decision log → short brief. |
| **3 — strategic** | the thesis, how the portfolio is split, the reserve design, the co-sponsor range method, anything that goes into the IPS | Full protocol below, with parallel subagents. |

### Full protocol (Tier 3)

1. **Frame it.** Write the question, what depends on it, and the deadline it has
   to be answered by.
2. **Gather evidence.** Researchers and the quant-modeler in parallel. Every
   number goes to `03-modeling/`, every source gets cited.
3. **Decide provisionally.** Write the decision and the reasoning.
4. **Attack it.** `red-team` (independent), `judge-panel`, and `rules-auditor` if
   it touches trades or deliverables. All in parallel.
5. **Revise or reverse.** Answer every objection in writing, or change the
   decision.
6. **Log it** in `99-admin/decision-log.md`: options, decision, reasoning,
   evidence, strongest objection and the answer, the "revisit when" trigger.
7. **Brief the humans** in `06-team/briefings/`, checked by `beginner-reader`.
   Include the exact actions they need to take.

### Things that are never Tier 1
- Anything entering the IPS — frozen on 6 Nov.
- Any trade — every trade leaves a verified Trading Note behind it.
- Anything that contradicts an earlier decision — it's a reversal, and gets
  logged as one.

---

## Part 4 — Standards for everything I produce

- **Reproducible.** Every number traces to a script or a cited source. Scripts
  save their output to `03-modeling/output/`.
- **Dated.** Market figures move fast this cycle; every one carries a date.
- **Labelled.** Fact / market price / our choice / assumption / inference.
- **Steelmanned.** The best case against sits next to every conclusion.
- **Aimed at a deliverable.** Name which deliverable and criterion each piece of
  work serves.
