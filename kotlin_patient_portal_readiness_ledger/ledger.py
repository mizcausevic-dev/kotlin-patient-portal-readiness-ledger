from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PortalFinding:
    lane_id: str
    surface: str
    score: float
    posture: str
    owner: str
    next_action: str


@dataclass(frozen=True)
class PortalSummary:
    estate: str
    aggregate_score: float
    blocked_lanes: int
    accessibility_failures: int
    primary_recommendation: str
    findings: list[PortalFinding]


def _num(lane: dict[str, Any], key: str) -> float:
    try:
        return float(lane[key])
    except KeyError as exc:
        raise ValueError(f"Missing required lane field: {key}") from exc


def score_lane(lane: dict[str, Any]) -> PortalFinding:
    blockers = _num(lane, "release_blockers") * 8.5
    accessibility = _num(lane, "accessibility_failures") * 3.2
    consent = _num(lane, "consent_copy_gaps") * 6.0
    delivery = _num(lane, "message_delivery_fail_percent") * 2.2
    crash = max(0, 99 - _num(lane, "crash_free_percent")) * 4.0
    score = round(min(100.0, blockers + accessibility + consent + delivery + crash), 2)
    posture = "block" if score >= 70 else "watch" if score >= 45 else "ready"
    return PortalFinding(
        lane_id=str(lane["lane_id"]),
        surface=str(lane["surface"]),
        score=score,
        posture=posture,
        owner=str(lane["owner"]),
        next_action=str(lane["next_action"]),
    )


def build_summary(payload: dict[str, Any]) -> PortalSummary:
    lanes = payload.get("lanes") or []
    if not lanes:
        raise ValueError("At least one patient portal readiness lane is required.")
    findings = sorted((score_lane(lane) for lane in lanes), key=lambda item: item.score, reverse=True)
    aggregate = round(sum(item.score for item in findings) / len(findings), 2)
    blocked = sum(1 for item in findings if item.posture == "block")
    accessibility_failures = sum(int(_num(lane, "accessibility_failures")) for lane in lanes)
    return PortalSummary(
        estate=str(payload.get("estate", "Patient portal readiness estate")),
        aggregate_score=aggregate,
        blocked_lanes=blocked,
        accessibility_failures=accessibility_failures,
        primary_recommendation=f"{findings[0].lane_id}: {findings[0].next_action}",
        findings=findings,
    )

