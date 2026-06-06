import json
import unittest
from pathlib import Path

from kotlin_patient_portal_readiness_ledger import build_summary, score_lane


FIXTURE = json.loads(Path("fixtures/portal_lanes.json").read_text(encoding="utf-8"))


class PatientPortalReadinessTests(unittest.TestCase):
    def test_prioritizes_mobile_reschedule(self) -> None:
        summary = build_summary(FIXTURE)
        self.assertEqual(summary.findings[0].lane_id, "mobile-appointment-reschedule")
        self.assertEqual(summary.blocked_lanes, 2)
        self.assertEqual(summary.accessibility_failures, 18)
        self.assertIn("reschedule consent copy", summary.primary_recommendation)

    def test_secure_message_reply_is_ready(self) -> None:
        finding = score_lane(FIXTURE["lanes"][2])
        self.assertEqual(finding.posture, "ready")
        self.assertLess(finding.score, 45)

    def test_requires_lane(self) -> None:
        with self.assertRaisesRegex(ValueError, "At least one patient portal readiness lane is required."):
            build_summary({"lanes": []})


if __name__ == "__main__":
    unittest.main()
