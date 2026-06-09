# kotlin-patient-portal-readiness-ledger

[![ci](https://github.com/mizcausevic-dev/kotlin-patient-portal-readiness-ledger/actions/workflows/ci.yml/badge.svg)](https://github.com/mizcausevic-dev/kotlin-patient-portal-readiness-ledger/actions/workflows/ci.yml)
[![pages](https://github.com/mizcausevic-dev/kotlin-patient-portal-readiness-ledger/actions/workflows/pages.yml/badge.svg)](https://github.com/mizcausevic-dev/kotlin-patient-portal-readiness-ledger/actions/workflows/pages.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)

Kotlin Patient Portal Readiness Ledger turns mobile release blockers, accessibility failures, consent copy gaps, message delivery failures, and crash-free posture into one board-readable release proof.

## What this product does

This repo packages patient portal release risk for executives, product leaders, patient-access teams, and technical reviewers. It answers whether a mobile portal lane is safe enough to launch, where patient trust or access may break, and which owner needs to clear the next release blocker before the update becomes patient-visible.

From a SaaS go-to-market and product marketing lens, the page turns Kotlin/mobile portal work into a clear buyer story: appointment flow, consent language, accessibility, message delivery, and crash-free posture are not separate technical chores. They are the operating proof behind patient retention, care access, support load, and trust.

From a technical lens, the repo keeps the claim inspectable. It includes a Kotlin contract, Python scoring logic, SQL review queries, fixtures, unit tests, smoke checks, generated screenshots, and a static public proof surface. No PHI or production portal data is included.

## Why this exists

- Patient portal risk gets expensive when release blockers, accessibility, consent language, and messaging reliability are reviewed separately.
- Kotlin is a direct signal for mobile and Android patient portal work.
- This repo gives practical HealthTech / patient access / Kotlin proof without exposing PHI or production portal data.
- The common pattern across these Kinetic Gain repos is to model an operational lane, score the exposed risk, identify the owner, state the next action, and publish readable proof for both non-technical leaders and technical reviewers.

## Screenshots

![Overview proof](screenshots/01-overview-proof.png)

![Portal proof](screenshots/02-ledger-proof.png)

## Local run

```bash
python -m pip install -e .
python -m unittest discover -s tests
python scripts/run_demo.py
python scripts/check_sql.py
python scripts/check_kotlin_contract.py
python scripts/prerender.py
python scripts/smoke_check.py
```

## Board question answered

> Which patient portal release lanes threaten access, consent, accessibility, and trust before the next mobile launch?
