import tempfile
import unittest
from pathlib import Path

from tools.check_codex_environment import REQUIRED_FILES, check_environment


class CodexEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        for filename in REQUIRED_FILES:
            target = self.root / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("fixture\n", encoding="utf-8")

    def test_profile_can_run_without_search_or_pdf_tools(self):
        report = check_environment(self.root, "profile", which=lambda name: None)
        self.assertTrue(report["ready"])

    def test_application_reports_missing_compilers(self):
        def installed(name):
            return None if name in {"xelatex", "lualatex"} else f"/tools/{name}"

        report = check_environment(self.root, "application", which=installed)
        self.assertFalse(report["ready"])
        self.assertEqual(set(report["missing_tools"]), {"xelatex", "lualatex"})

    def test_custom_pdf_toolchain_does_not_require_stock_compilers(self):
        report = check_environment(self.root, "pdf", which=lambda name: f"/tools/{name}")
        self.assertTrue(report["ready"])
        self.assertNotIn("lualatex", report["tools"])

    def test_search_requires_bun_without_latex(self):
        report = check_environment(
            self.root, "search", which=lambda name: "/tools/bun" if name == "bun" else None
        )
        self.assertTrue(report["ready"])

    def test_missing_workflow_is_not_a_ready_checkout(self):
        (self.root / ".claude/commands/apply.md").unlink()
        report = check_environment(self.root, "profile")
        self.assertFalse(report["ready"])
        self.assertIn(".claude/commands/apply.md", report["missing_files"])

    def test_old_python_is_not_ready(self):
        report = check_environment(self.root, "profile", version=(3, 9, 20))
        self.assertFalse(report["ready"])


if __name__ == "__main__":
    unittest.main()
