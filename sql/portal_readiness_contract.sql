create view patient_portal_readiness_ledger as
select
  lane_id,
  surface,
  release_blockers,
  accessibility_failures,
  consent_copy_gaps,
  message_delivery_fail_percent,
  crash_free_percent,
  owner,
  next_action,
  case
    when release_blockers >= 5 or accessibility_failures >= 10 then 'block'
    when release_blockers >= 2 or accessibility_failures >= 4 then 'watch'
    else 'ready'
  end as release_posture
from reviewed_patient_portal_release_lanes;

