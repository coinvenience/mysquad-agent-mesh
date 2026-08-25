# Stage 02: Pipeline & Task Dispatch
## Input
- Agent Task Queue (`agent_tasks` table)
- Claimed board items from `sessions/board/NEXT_SESSION_START.md`

## Process
- Match task domain with agent soul profile (HermesLocal for ops/git, Cursor for code, Grok for build).
- Execute task with idempotency verification.

## Output
- Verified execution artifact & commit trace.
