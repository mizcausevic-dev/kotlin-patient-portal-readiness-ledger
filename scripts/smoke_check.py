from pathlib import Path

html = Path("site/index.html").read_text(encoding="utf-8")
required = [
    "Kotlin Patient Portal Readiness Ledger",
    "Portal release risk stays visible",
    "mobile-appointment-reschedule",
    "lab-result-notification",
]
missing = [token for token in required if token not in html]
if missing:
    raise SystemExit(f"missing site marker(s): {', '.join(missing)}")
print("smoke ok")

