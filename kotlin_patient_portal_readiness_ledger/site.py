from __future__ import annotations

import html

from .ledger import PortalSummary


def render_site(summary: PortalSummary) -> str:
    cards = "\n".join(
        f"""<article class="lane {finding.posture}">
<span>{html.escape(finding.posture)}</span>
<h3>{html.escape(finding.lane_id)}</h3>
<p>{html.escape(finding.surface)} resolves into a {finding.score:g} readiness score.</p>
<dl><div><dt>Owner</dt><dd>{html.escape(finding.owner)}</dd></div><div><dt>Score</dt><dd>{finding.score:g}</dd></div></dl>
<strong>{html.escape(finding.next_action)}</strong>
</article>"""
        for finding in summary.findings
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Kotlin Patient Portal Readiness Ledger</title><meta name="description" content="Kotlin patient portal readiness ledger for mobile release risk, consent checks, accessibility, and appointment-flow reliability."/><style>
:root{{--bg:#050812;--panel:#0d1727;--text:#f4f1ea;--muted:#a8b3c7;--cyan:#25d7ef;--green:#58f0b3;--pink:#ff72b6;--line:rgba(37,215,239,.24)}}*{{box-sizing:border-box}}body{{margin:0;font-family:"Segoe UI",sans-serif;color:var(--text);background:radial-gradient(circle at 82% 8%,rgba(255,114,182,.13),transparent 32rem),radial-gradient(circle at 14% 8%,rgba(37,215,239,.14),transparent 30rem),var(--bg)}}main{{width:min(1180px,calc(100% - 40px));margin:0 auto;padding:56px 0}}.hero,.lane{{background:linear-gradient(135deg,rgba(13,23,39,.96),rgba(8,11,24,.92));border:1px solid var(--line);border-radius:28px}}.hero{{padding:clamp(30px,5vw,64px)}}.kicker{{color:var(--green);font-family:Consolas,monospace;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase}}h1{{max-width:1040px;margin:18px 0;font-size:clamp(3rem,7.2vw,6.2rem);line-height:.92;letter-spacing:-.075em}}.lede{{max-width:790px;color:var(--muted);font-size:1.24rem;line-height:1.7}}.metrics,.grid{{display:grid;gap:16px}}.metrics{{grid-template-columns:repeat(4,1fr);margin-top:34px}}.metric,.lane{{background:rgba(13,23,39,.9);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:22px}}.metric small,dt{{color:var(--muted);text-transform:uppercase;letter-spacing:.12em;font-size:.75rem}}.metric b{{display:block;margin-top:10px;font-size:2rem}}.grid{{grid-template-columns:repeat(3,1fr);margin-top:22px}}.lane{{min-height:330px}}.lane span{{color:var(--cyan);font-family:Consolas,monospace;text-transform:uppercase;letter-spacing:.14em;font-size:.76rem}}.lane.block{{border-color:rgba(255,114,182,.5)}}.lane.watch{{border-color:rgba(157,140,255,.44)}}.lane.ready{{border-color:rgba(88,240,179,.45)}}h3{{font-size:1.45rem;margin:14px 0 10px}}p{{color:var(--muted);line-height:1.6}}dl{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0}}dd{{margin:5px 0 0;font-size:1.1rem;font-weight:800}}footer{{margin-top:34px;color:var(--muted);font-family:Consolas,monospace}}@media(max-width:900px){{.metrics,.grid,dl{{grid-template-columns:1fr}}}}
</style></head><body><main><section class="hero"><div class="kicker">Kotlin / HealthTech / Patient Portal</div><h1>Portal release risk stays visible before patient access breaks.</h1><p class="lede">Kotlin Patient Portal Readiness Ledger turns mobile release blockers, accessibility failures, consent copy gaps, message delivery failures, and crash-free posture into one board-readable release proof.</p><div class="metrics"><div class="metric"><small>Aggregate score</small><b>{summary.aggregate_score:g}</b></div><div class="metric"><small>Blocked lanes</small><b>{summary.blocked_lanes}</b></div><div class="metric"><small>A11y failures</small><b>{summary.accessibility_failures}</b></div><div class="metric"><small>Top lane</small><b>{html.escape(summary.findings[0].lane_id)}</b></div></div></section><section class="grid">{cards}</section><footer>Primary recommendation: {html.escape(summary.primary_recommendation)}</footer></main></body></html>"""

