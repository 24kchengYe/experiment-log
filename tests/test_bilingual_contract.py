from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class BilingualContractTests(unittest.TestCase):
    def test_every_reference_and_template_has_chinese_version(self) -> None:
        for folder in (ROOT / "references", ROOT / "assets"):
            english_files = [
                path for path in folder.glob("*.md") if not path.name.endswith(".zh-CN.md")
            ]
            missing = [
                path.name
                for path in english_files
                if not path.with_name(f"{path.stem}.zh-CN.md").exists()
            ]
            self.assertEqual(missing, [], f"missing Chinese counterparts under {folder.name}")

    def test_chinese_master_preserves_evidence_constraints(self) -> None:
        text = (ROOT / "SKILL.zh-CN.md").read_text(encoding="utf-8")
        required = (
            "claim–evidence map",
            "hostile-review",
            "不得删除不利证据或必要披露",
            "AI式防御性写作",
            "不自动授权改写指南或论文",
            "程序状态",
            "证据结果",
            "主张资格",
        )
        for phrase in required:
            self.assertIn(phrase, text)

    def test_chinese_markdown_local_links_resolve(self) -> None:
        paths = [ROOT / "SKILL.zh-CN.md"]
        paths.extend((ROOT / "references").glob("*.zh-CN.md"))
        paths.extend((ROOT / "assets").glob("*.zh-CN.md"))
        missing: list[str] = []
        for path in paths:
            text = path.read_text(encoding="utf-8")
            links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", text)
            missing.extend(
                f"{path.relative_to(ROOT)} -> {target}"
                for target in links
                if not (path.parent / target).resolve().exists()
            )
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
