import json
from pathlib import Path

from kotlin_patient_portal_readiness_ledger import build_summary


summary = build_summary(json.loads(Path("fixtures/portal_lanes.json").read_text(encoding="utf-8")))
print(f"estate={summary.estate}")
print(f"score={summary.aggregate_score:g}")
print(f"blocked={summary.blocked_lanes}")
print(f"accessibility_failures={summary.accessibility_failures}")
print(f"recommendation={summary.primary_recommendation}")

