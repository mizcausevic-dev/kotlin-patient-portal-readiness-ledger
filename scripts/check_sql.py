from pathlib import Path

sql = Path("sql/portal_readiness_contract.sql").read_text(encoding="utf-8").lower()
required = ["create view", "patient_portal_readiness_ledger", "accessibility_failures", "consent_copy_gaps", "crash_free_percent"]
missing = [token for token in required if token not in sql]
if missing:
    raise SystemExit(f"missing sql contract token(s): {', '.join(missing)}")
print("sql contract ok")

