# Provider and worker contract

Canonical provider: `GBOGEB/gg_MATH`.
Canonical skill SSOT: `GBOGEB/skills/skills/math`.
Orchestration: `GBOGEB/pipeline-automation-hub`.

Worker envelope:
```json
{
  "schema": "gbogeb.skill.invoke.v1",
  "skill": "math",
  "task_id": "caller-defined",
  "source_repo": "GBOGEB/example",
  "source_ref": "exact SHA or ref",
  "topic": "PCA",
  "maturity": "DEEP_DIVE",
  "inputs": {},
  "authority_transfer": false
}
```

Required receipt fields: schema, skill, task_id, source_repo, source_ref, resolved_skill_path, authority_transfer, status. A resolution receipt proves only that the worker selected and validated the skill contract; it does not prove mathematical correctness or engineering acceptance.
