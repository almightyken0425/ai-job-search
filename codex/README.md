# Codex Core Workflow

- This adapter reuses the upstream profile, evaluation rules, workflow commands, and templates.
- Run Codex in this repository so its project skills can be discovered.
- Shared source documents remain in their upstream locations.
- The core workflow covers profile setup, application documents, independent review, and outcome recording.

## Usage

| Request | Skill |
| --- | --- |
| 建立求職資料 | `job-setup` |
| 評估職缺或製作履歷與求職信 | `job-apply` |
| 記錄投遞或更新求職結果 | `job-outcome` |

- Mention the skill through the host's skill selector or request the task naturally.
- Codex CLI also supports explicit skill mentions.

```text
$job-setup Import the career documents already provided.
$job-apply Evaluate this posting and prepare application PDFs if eligible.
$job-outcome Record that the application was submitted today.
```

- Real candidate data requires private storage or explicitly confirmed local-only handling.
- The adapter does not submit applications or send follow-up messages.
- Gmail, Notion, reset, and broader workflow adaptation remain outside this delivery.

---

## Environment

- Use Python 3.10 or later.
- Install LaTeX and Poppler before generating and inspecting stock PDFs.
- Install Bun when using the existing portal search tools.
- The environment checker reports missing tools without installing software or changing permissions.

```bash
python3 tools/check_codex_environment.py --stage profile
python3 tools/check_codex_environment.py --stage application
python3 tools/check_codex_environment.py --stage search
```

- Custom templates may use a different compiler.
- In that case, run the PDF-tool check and verify the declared compiler separately.

```bash
python3 tools/check_codex_environment.py --stage pdf
```

- Consult the upstream [installation guide](../SETUP.md) for template dependencies.
- Read the [runtime adapter](runtime.md) for tool substitutions and candidate-data boundaries.
- Follow [PDF verification](pdf_verification.md) for rendering and inspection.

---

## Validation

- Run the existing repository checks and the Codex helper tests.
- PyYAML is required by the skill linter and the skill-creator validator.

```bash
python3 tools/lint_skills.py
python3 tools/security_guards.py
python3 -m unittest discover -s tests -t .
```

- Behavioral validation uses a copied repository and fictional career documents.
- Verify setup populates all canonical targets before running an application.
- Verify both PDFs, independent review, the draft record, and a reported submission update.
- Repeat drafting after submission to check that status and submission date remain unchanged.
- Keep generated test artifacts outside the maintained checkout.
