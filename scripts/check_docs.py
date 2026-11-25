"""Check the documentation navigation, relative Markdown links and JSON syntax."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
nav = json.loads((docs / "navigation.json").read_text())
pages = [p for section in nav for p in section["pages"]]
assert len(pages) == len(set(pages)), "Duplicate navigation entry"
actual = {str(p.relative_to(docs)) for p in docs.rglob("*.md") if p != docs / "README.md"}
assert set(pages) == actual, f"Navigation mismatch: {set(pages) ^ actual}"
for page in pages:
    text = (docs / page).read_text()
    assert text.startswith("---\n") and "title:" in text.split("---", 2)[1], page
    assert "description:" in text.split("---", 2)[1], page
for path in root.rglob("*.json"):
    json.loads(path.read_text())
for path in root.rglob("*.md"):
    text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#") or link.startswith("mailto:"):
            continue
        target = link.split("#", 1)[0]
        if target:
            assert (path.parent / target).exists(), f"{path}: missing {target}"
print("Documentation navigation, relative links and JSON syntax OK")
