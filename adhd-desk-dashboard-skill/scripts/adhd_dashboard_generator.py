#!/usr/bin/env python3
"""Generate markdown scaffolds for an ADHD/TDAH-friendly desk dashboard."""
from pathlib import Path

OUT = Path("generated")
OUT.mkdir(exist_ok=True)

workflow_rows = [
    ("DataClean", "45min/d", "Raw notes/chats/files", "Classified knowledge", "Drive/Vault", "Classify FACT/HYPOTHESIS/DECISION/ACTION", "Inbox reduced; reusable items saved"),
    ("ContentCreation", "Morning", "Topic/current insight", "Content batch", "Pipeline", "Batch channel-specific posts", "Published/scheduled; URLs saved"),
    ("OpsAdmin", "90min/d", "Email/accounts/backlog", "Clean admin state", "Linear/Agenda", "Run admin loop", "Tomorrow prepared"),
    ("Analytics", "Weekly", "URLs/metrics", "Baseline metrics", "Metrics table", "Capture metric deltas", "Next experiment selected"),
    ("Review", "Weekly", "Done cards/issues", "Decision log", "Vault", "Review keep/change/stop", "Decisions recorded")
]

md = ["# Capacity Table", "", "| Workflow | Time | Input | Output | Save | Command | DoD |", "|---|---:|---|---|---|---|---|"]
for row in workflow_rows:
    md.append("| " + " | ".join(row) + " |")

(OUT / "capacity-table.md").write_text("\n".join(md), encoding="utf-8")
print(f"Generated {(OUT / 'capacity-table.md').resolve()}")
