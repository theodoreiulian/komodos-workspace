# AI use log

**Why this exists.** On 29 Sep 2026 the Team Leader made Claude (Anthropic) the
team's lead strategist. This is a factual activity record that helps future
sessions understand what work was done and why.

Each entry records what the AI did, which files it produced, and which decisions
it made.

| Date | Model | What Claude did | Outputs | Decisions made |
|---|---|---|---|---|
| 2026-09-16 | Claude Opus 5 | Set up the workspace; wrote up the rules, criteria and client brief; research base (past winners, differentiation angles, knowledge base, macro snapshot); core model | `00-competition/`, `01-research/`, `03-modeling/src/laura_core_model.py` | None (research only) |
| 2026-09-23 | Claude Opus 5 | Barbell comparison model; wrote up the team meeting's decisions | `03-modeling/src/barbell_comparison.py` | None (team decided; since cancelled) |
| 2026-09-29 | Claude Opus 5.5 | Restructured the repo with Claude as lead strategist; cancelled earlier decisions at the Team Leader's instruction; wrote the charter, playbook and subagent definitions | `CLAUDE.md`, `99-admin/*`, `.claude/agents/*` | Working method only; no investment decisions |
| 2026-09-29 | Claude Opus 5.5 | Browsed the team's StockTrak account to list tradable bonds and target-maturity ETFs; web search for fund tickers | `04-portfolio/wins-instruments.md`, `06-team/punchlist.md` | None (fact-finding) |
| 2026-09-30 | Claude Opus 5.5 | Revised the Trading Note workflow; brought the thesis decision forward to 1 Oct; wrote team tasks P2–P7 | `CLAUDE.md`, `04-portfolio/README.md`, `06-team/*`, `99-admin/state.md` | Schedule only; no investment decisions |
| 2026-09-30 | Claude Opus 5.5 | Thesis decision (Tier 3): research on yields (researcher subagent) and on expected equity returns (web search; subagent failed on a usage limit); built the thesis model with ladder optimisation and a 4-strategy Monte Carlo; two red-team passes and a judge panel; rebuilt the model after the red-team findings; wrote the brief, the session pack and primers A–D | `03-modeling/src/thesis_decision_2026_09_30.py` + output, `06-team/briefings/2026-09-30-lock-in-the-promise.md`, `06-team/sessions/*`, `06-team/primers/*`, `02-strategy/proposal-2026-09-30.md`, updated treasury curve CSV | **Q2/Q3: lock in all ten payments at the start (Promise Portfolio); promise-lock principle; 2/3-scale WInS convention** |
| 2026-10-07 | Claude Opus 5.5 | Recorded the fifth team member (Marc); checked the team-size, age and roster-change rules on Wharton's Rules & Roles page; wrote Marc's catch-up plan (an email to Wharton about the roster was drafted, then dropped when the Team Leader produced Wharton's confirmation email allowing edits until 9 Oct) | `00-competition/competition-brief.md` §3, `00-competition/deliverable-specs.md` §1, `06-team/onboarding-marc.md`, `99-admin/roster-confirmation-email.md`, `06-team/punchlist.md` P8–P9, `99-admin/state.md` | None (admin only; no investment decisions) |
| 2026-10-07 | Codex | Audited the complete repository and removed AI-specific restrictions from charters, competition summaries, agent definitions, research rules, portfolio and deliverable workflows, team materials and administration; confirmed the archived source PDFs contain no AI-policy text | `AGENTS.md`, `CLAUDE.md`, `README.md`, `00-competition/`, `.claude/agents/`, `.codex/agents/`, `01-research/`, `02-strategy/`, `04-portfolio/`, `05-deliverables/`, `06-team/`, `99-admin/` | AI authority now covers research, decisions, drafting, editing and review across the entire project |
| 2026-10-07 | Codex | Made the repository the exclusive source of Wharton competition rules and prohibited every project agent from consulting or enforcing outside rule sources | `00-competition/RULE-AUTHORITY.md`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `99-admin/playbook.md`, `.claude/agents/*`, `.codex/agents/*`, `99-admin/state.md`, `99-admin/decision-log.md` | Repo-only competition-rule authority adopted |
