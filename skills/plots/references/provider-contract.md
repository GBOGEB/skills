# Provider and worker contract

Canonical skill SSOT: `GBOGEB/skills/skills/plots`.
Interactive implementation reference: Plotly/`GBOGEB/plotly.py` where relevant.
Static renderer: Matplotlib from the execution environment.
Orchestration: `GBOGEB/pipeline-automation-hub`.

Worker envelope uses schema `gbogeb.skill.invoke.v1` and `skill: plots`. Include `task_id`, `source_repo`, `source_ref`, `plot_purpose`, `clock` when temporal, `inputs`, and `authority_transfer:false`.

A runner may resolve and validate the bundle. An agent or explicit rendering script performs the semantic plotting work.
