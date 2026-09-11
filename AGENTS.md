---
framework_version: 1.1.0
---

# Agent Guidelines: AI Job Search

- This workspace manages job searches, applications, CVs, cover letters, and interview preparation.

## Shared Sources

- Keep one copy of each candidate fact and workflow rule across agent runtimes.
- Read the candidate profile in [CLAUDE.md](CLAUDE.md) when performing job-search work.
- Read the relevant [profile and methodology references](.claude/skills/job-application-assistant/) for the selected workflow.
- Follow the canonical [commands](.claude/commands/) and [workflow skills](.claude/skills/).
- Preserve these source locations so upstream updates remain comparable.
- Candidate facts remain subject to the grounding rules in the canonical application workflow.
- Repository maintenance does not authorize running onboarding or personalizing the candidate templates.

---

## Codex Entry Points

- Use [job-setup](.agents/skills/job-setup/SKILL.md) to create or update a candidate profile.
- Use [job-apply](.agents/skills/job-apply/SKILL.md) to evaluate a posting or prepare application documents.
- Use [job-outcome](.agents/skills/job-outcome/SKILL.md) to record submission, interview stages, or application results.
- Load the [Codex runtime adapter](codex/runtime.md) before executing those canonical workflows.
- The adapter changes runtime operations without duplicating the underlying evaluation and writing rules.
- Follow the [Codex usage guide](codex/README.md) for setup and validation commands.
- Other agent runtimes continue using the canonical workflows directly.

---

## Portal Search

- Portable portal tools remain under [.agents/skills](.agents/skills/).
- The canonical [scraper workflow](.claude/skills/job-scraper/SKILL.md) orchestrates installed portal tools.
- The core Codex adapter does not automatically run searches or connect external accounts.
