---
name: job-setup
description: Create or update a job-search candidate profile from career documents or an interview. Use for 求職建檔 or 更新求職資料. Repository installation and coding-project setup are outside this skill.
---

# Job Profile Setup

- Read the [runtime adapter](../../../codex/runtime.md) before using the canonical workflow.
- Run the environment check for the `profile` stage from the repository root.

```bash
python3 tools/check_codex_environment.py --stage profile
```

- Read the complete [onboarding workflow](../../../.claude/commands/setup.md).
- Use supplied documents or an explicitly selected interview path.
- Honor an existing path selection instead of repeating the welcome menu.
- Follow the canonical additive-update and factual-conflict rules.
- Read each target document completely before updating its profile sections.
- Reuse confirmed information without inventing missing experience or contact details.
- Report the changed profile sections and unresolved factual questions.
- Do not start an application unless requested.
