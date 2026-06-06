# Architecture

This repo is a synthetic patient portal readiness surface. It does not connect to EHRs, portals, messaging systems, or production patient data.

## Layers

- `fixtures/portal_lanes.json` provides synthetic reviewed portal release lanes.
- `kotlin/PortalReadiness.kt` documents the mobile release-readiness contract.
- `kotlin_patient_portal_readiness_ledger/ledger.py` scores operator posture.
- `sql/portal_readiness_contract.sql` names the reviewed fields expected from a warehouse view.
- `scripts/prerender.py` writes the static GitHub Pages artifact.

## Safety boundary

No PHI, patient identifiers, auth secrets, portal tokens, EHR exports, or production messages belong in this repository.

