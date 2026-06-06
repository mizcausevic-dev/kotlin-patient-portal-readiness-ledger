from pathlib import Path

source = Path("kotlin/PortalReadiness.kt").read_text(encoding="utf-8")
required = ["data class PortalLane", "fun readinessBlocked", "fun readinessReason", "accessibilityFailures", "consentCopyGaps"]
missing = [token for token in required if token not in source]
if missing:
    raise SystemExit(f"missing Kotlin contract token(s): {', '.join(missing)}")
print("kotlin contract ok")

