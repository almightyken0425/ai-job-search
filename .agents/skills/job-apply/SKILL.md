---
name: job-apply
description: Evaluate a job posting against a candidate profile or create tailored application PDFs with independent review. Use for 職缺評估 or 製作履歷與求職信. Does not submit applications.
---

# Job Application

- Read the [runtime adapter](../../../codex/runtime.md).
- Read the complete [application workflow](../../../.claude/commands/apply.md).
- Resolve arguments from the current request and confirmed conversation context.
- Check that the candidate profile contains facts before evaluating fit.
- Route an empty profile to `job-setup` instead of drafting from placeholders.
- Follow the canonical eligibility gates and weighted evaluation.
- An evaluation-only request ends after presenting fit, strengths, and gaps.
- A request explicitly including drafting already authorizes the drafting stage.
- Respect a later rejection or an unresolved eligibility failure.
- Resolve the active templates before checking compiler availability.
- For stock templates, run the environment check for the `application` stage.

```bash
python3 tools/check_codex_environment.py --stage application
```

- For a custom template, use `--stage pdf` and check its declared compiler separately.
- Preserve the independent reviewer stage described by the runtime adapter.
- Follow [PDF verification](../../../codex/pdf_verification.md) for compilation, rendering, and text checks.
- Record the draft and verbatim posting through the canonical recording step.
- End with PDF locations, verification results, and the recorded draft status.
- Distinguish pending work from verified output when any stage cannot finish.
