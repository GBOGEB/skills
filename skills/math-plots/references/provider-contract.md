# Provider and worker contract

Canonical skill SSOT: `GBOGEB/skills/skills/math-plots`.
Math provider: `GBOGEB/gg_MATH`.
Interactive plotting reference: Plotly/`GBOGEB/plotly.py` where relevant.
Orchestration: `GBOGEB/pipeline-automation-hub`.

Invocation schema: `gbogeb.skill.invoke.v1`, `skill: math-plots`.
Required: task_id, source_repo, source_ref, topic, maturity, plot_purpose, authority_transfer=false. Optional: clock, requested_visuals, inputs.

Resolution proves bundle selection only. Mathematical verification and render QA remain separate receipts.
