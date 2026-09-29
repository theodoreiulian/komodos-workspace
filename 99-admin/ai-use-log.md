# AI use log

**Why this exists.** Wharton requires all AI-generated material to be cited in
the Final Report's Works Cited, and treats undisclosed AI work as academic
dishonesty. On 29 Sep 2026 the Team Leader made Claude (Anthropic) the team's
lead strategist, so AI's contribution to this project is large. It must be
disclosed accurately, and this log is the record we will draw on to do that.

**Rules.** Claude adds one line per working session: what it did, which files
it produced, and which decisions it made. Keep it factual. Never delete lines.

| Date | Model | What Claude did | Outputs | Decisions made |
|---|---|---|---|---|
| 2026-09-16 | Claude Opus 5 | Set up the workspace; wrote up the rules, criteria and client brief; research base (past winners, differentiation angles, knowledge base, macro snapshot); core model | `00-competition/`, `01-research/`, `03-modeling/src/laura_core_model.py` | None (research only) |
| 2026-09-23 | Claude Opus 5 | Barbell comparison model; wrote up the team meeting's decisions | `03-modeling/src/barbell_comparison.py` | None (team decided; since cancelled) |
| 2026-09-29 | Claude Opus 5.5 | Restructured the repo with Claude as lead strategist; cancelled earlier decisions at the Team Leader's instruction; wrote the charter, playbook and subagent definitions | `CLAUDE.md`, `99-admin/*`, `.claude/agents/*` | Working method only; no investment decisions |
| 2026-09-29 | Claude Opus 5.5 | Browsed the team's StockTrak account (read-only) to list tradable bonds and target-maturity ETFs; web search for fund tickers | `04-portfolio/wins-instruments.md`, `06-team/punchlist.md` | None (fact-finding) |
