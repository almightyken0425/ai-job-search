# PDF Verification in Codex

- Preserve the active template's declared compiler and page limits.
- Stock CVs use `lualatex` and exactly two pages.
- Stock cover letters use `xelatex` and exactly one page.
- Read the candidate's actual contact values for text checks.

## Compile

- Compile from the source directory so bundled classes and fonts resolve correctly.
- Use separate shell calls for the two stock documents.
- Substitute actual filenames for the example arguments.

```bash
lualatex -interaction=nonstopmode -halt-on-error main_example.tex
```

```bash
xelatex -interaction=nonstopmode -halt-on-error cover_example.tex
```

- A custom template keeps its declared command instead of either stock command.
- Inspect compiler errors before continuing.
- Do not replace a failed template with an unrelated PDF generator.

---

## Check Text and Pages

- Run the repository verifier against both generated documents from the repository root.
- Replace the example filenames and contact value with the generated application values.

```bash
python3 tools/verify_pdf.py cv/main_example.pdf --pages 2 --min-chars 100 --contains your.email@example.com
python3 tools/verify_pdf.py cover_letters/cover_example.pdf --pages 1 --min-chars 100
```

- Adapt page counts to the active template when it overrides the stock limits.
- Extract UTF-8 text for the canonical keyword and reading-order checks.

```bash
pdftotext -layout -enc UTF-8 cv/main_example.pdf -
```

- A passing text check does not establish visual correctness.
- Missing extraction tools must be disclosed as an incomplete mechanical check.

---

## Inspect Pages

- Create a gitignored preview directory under `reports/pdf_checks/` for the current application.
- Render every page with Poppler.
- Use different output prefixes for the CV and cover letter.

```bash
pdftoppm -scale-to 1600 -png cv/main_example.pdf reports/pdf_checks/cv
pdftoppm -scale-to 1600 -png cover_letters/cover_example.pdf reports/pdf_checks/cover
```

- Open every resulting image with the host's image-viewing capability.
- Apply the canonical checks for page breaks, orphaned headings, font consistency, and visible signatures.
- Revise, recompile, and inspect again when layout checks fail.
- Disclose unavailable image inspection instead of treating page count as a visual review.
- Keep sources and PDFs after successful verification.
- Remove only build artifacts belonging to this run when cleanup is necessary.
