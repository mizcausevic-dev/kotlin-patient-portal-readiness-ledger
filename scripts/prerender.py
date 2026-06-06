import json
from pathlib import Path

from kotlin_patient_portal_readiness_ledger import build_summary
from kotlin_patient_portal_readiness_ledger.site import render_site


payload = json.loads(Path("fixtures/portal_lanes.json").read_text(encoding="utf-8"))
Path("site").mkdir(exist_ok=True)
Path("site/index.html").write_text(render_site(build_summary(payload)), encoding="utf-8")

