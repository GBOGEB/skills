---
name: math-plots
description: Compose rigorous mathematical analysis with method-specific canonical and supplemental visualization. Use when ChatGPT or a mission worker must both perform/interpret mathematics and select or generate the correct Plotly/Matplotlib visual vocabulary, including PCA scree/loadings/scores, Bradley-Terry probability and comparison graphs, confidence forests, spectral plots, covariance heatmaps/ellipsoids, regression diagnostics, time-series/state-space views, dynamical phase portraits, Monte Carlo uncertainty, optimization surfaces, Bayesian diagnostics, and asymptotic regime maps.
---

# Math Plots

Compose the `math` and `plots` contracts without weakening either. The mathematical model determines the visual semantics; the visual layer must expose assumptions, uncertainty, geometry, temporal evolution and failure modes rather than merely restyle outputs.

## Execution contract

1. Resolve the mathematical topic and maturity band.
2. Execute or verify the mathematical object using the `math` rules.
3. Select a **canonical visual** expected for the method, then add only diagnostics that answer a distinct question.
4. Use the topic map in `references/method-visual-map.md`.
5. For temporal models, treat the clock explicitly and align component/subspace identity before animating apparent movement.
6. Produce Plotly interactive output for exploration and Matplotlib static output for governed snapshots when feasible.
7. Keep score space, loading space, parameter space, observation space and uncertainty space distinct.
8. Do not infer significance, importance, causality, rank certainty or acceptance from visual salience alone.
9. Preserve `authority_transfer=false` at this skill boundary.

## Composition rules

Load `references/method-visual-map.md` for topic-specific visuals, `references/temporal-3d.md` for temporal/3D/mesh/surface work, and `references/provider-contract.md` for mission workers. Use `scripts/skill_contract.py` to validate the composite invocation envelope.

## Rolling N+2 learning

When a mission uses repeated pulses/waves, load `references/forecast-n-plus-2.md`. Couple prediction, later actual outcome, forecast scoring, estimator update and the next two-step horizon. Keep model learning and visualization receipts separate but cross-linked.
