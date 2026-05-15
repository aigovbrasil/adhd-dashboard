from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "manifest.json",
    "references/adhd-design-principles.md",
    "references/workflow-protocol.md",
    "references/sources-and-safety.md",
    "scripts/adhd_dashboard_generator.py",
    "schemas/dashboard_schema.json"
]

def test_required_files_exist():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    assert not missing, f"Missing files: {missing}"
