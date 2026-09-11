---
name: job-outcome
description: Record submission dates, interview stages, and outcomes for tracked job applications. Also draft requested follow-up notes. Use for 記錄投遞 or 更新求職結果. Does not send messages or infer acceptance.
---

# Application Outcomes

- Read the [runtime adapter](../../../codex/runtime.md).
- Read the complete [outcome workflow](../../../.claude/commands/outcome.md).
- Match the application using the canonical tracker and archive rules.
- Ask for clarification if multiple applications match the supplied description.
- Record only the submission date or result explicitly supplied by the user.
- Preserve all unrelated tracker fields and previously archived submitted materials.
- Treat follow-up messages as drafts for the user to send.
- Report the changed application and status without starting an external sync.
