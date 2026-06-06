data class PortalLane(
    val laneId: String,
    val releaseBlockers: Int,
    val accessibilityFailures: Int,
    val consentCopyGaps: Int,
    val crashFreePercent: Double
)

fun readinessBlocked(lane: PortalLane): Boolean {
    return lane.releaseBlockers > 0 &&
        (lane.accessibilityFailures >= 5 || lane.consentCopyGaps >= 2 || lane.crashFreePercent < 97.0)
}

fun readinessReason(lane: PortalLane): String {
    return when {
        lane.accessibilityFailures >= 5 -> "${lane.laneId}: accessibility regression"
        lane.consentCopyGaps >= 2 -> "${lane.laneId}: consent copy gap"
        lane.crashFreePercent < 97.0 -> "${lane.laneId}: crash-free posture below release threshold"
        else -> "${lane.laneId}: release posture ready"
    }
}

