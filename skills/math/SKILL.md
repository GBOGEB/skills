---
name: math
description: Deep mathematical analysis and governed method selection for PCA, Bradley-Terry, confidence intervals, eigen/spectral methods, matrix mathematics, ANOVA, covariance and multivariate inference, regression/GLMs, hypothesis testing, time series/state space, calculus/dynamics, Monte Carlo, information theory, optimization, Bayesian methods, and asymptotic/regime maps. Use when ChatGPT or a mission worker must derive, verify, compare, diagnose, or explain mathematics without needing a visualization as the primary output.
---

# Math

Treat `GBOGEB/gg_MATH` as the canonical executable/provider repository for this knowledge family. Treat this skill as the reusable reasoning and worker contract, not as authority to promote unverified research into engineering acceptance.

## Execution contract

1. Identify the mathematical topic and maturity band: `CORE`, `ADVANCED`, `DEEP_DIVE`, or `STRETCH`.
2. State assumptions, data geometry, units, and identifiability conditions before deriving or fitting.
3. Prefer exact identities/reference kernels before approximation or simulation.
4. Separate descriptive structure from inferential claims and causal claims.
5. For temporal or repeated fits, align identities before comparing coordinates: assignment -> sign/orientation -> congruence -> principal angles/Procrustes/subspace metrics as applicable.
6. Report uncertainty with the estimator that generated it; do not mix fixed-horizon CI, bootstrap intervals, posterior credible intervals, confidence sequences, and prediction intervals as if equivalent.
7. State validity domains, failure modes, and non-identifiability explicitly.
8. Never turn synthetic/reference agreement into QPS or engineering acceptance. Preserve `authority_transfer=false` unless separately governed.

## Topic routing

Load `references/deep-dive-map.md` for the topic-specific knowledge ladder and canonical diagnostics. Load `references/regime-and-temporal.md` for asymptotic, temporal, manifold, or multi-clock work. Load `references/provider-contract.md` when operating as a mission crew member or GitHub runner.

## Output minimum

Return, as relevant:
- mathematical object/model;
- assumptions and dimensions;
- governing equations/estimator;
- diagnostics and uncertainty;
- failure/degeneracy conditions;
- interpretation bounded to the evidence;
- runtime/provider pointer when execution is required.

## Worker invocation

For machine-facing mission work, emit or consume the JSON envelope documented in `references/provider-contract.md`. Use `scripts/skill_contract.py` to validate the envelope and produce a deterministic skill-resolution receipt.

## Rolling prediction and learning

For wave/pulse work that asks what comes next, use the rolling N+2 contract in `references/forecast-n-plus-2.md`. Preserve predictions before outcomes are known, score them against later actuals, and update calibration without rewriting history.
