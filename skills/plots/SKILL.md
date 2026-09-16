---
name: plots
description: Governed visualization design and implementation using Plotly for interactive/3D/temporal exploration and Matplotlib for deterministic static/publication output. Use when ChatGPT or a mission worker must choose, generate, review, or QA plots such as line/scatter/bar, box/violin, heatmaps, surfaces, meshes, contours, waterfall, Sankey, radial/polar, dependency/network, uncertainty, animation, or multi-panel scientific figures, independent of any one mathematical method.
---

# Plots

Treat visualization as an analytical instrument, not decoration. Plotly is the default interactive layer; Matplotlib is the default deterministic static/export layer. Use both for governed outward products when feasible.

## Execution contract

1. Identify the visual question: comparison, distribution, relationship, uncertainty, geometry, topology, flow, temporal evolution, regime boundary, or decomposition.
2. Choose the chart family from `references/visual-grammar.md`; do not select a chart merely because the library supports it.
3. Bind every axis, color, size, facet, frame and hover field to a declared variable and unit.
4. Distinguish wall time from ordered state clocks such as pulse, wave, PR, cycle or version.
5. For 3D, surfaces and meshes, verify that the third dimension is meaningful; do not manufacture a z-axis from styling.
6. Plot uncertainty and thresholds with explicit semantics.
7. Use Plotly for hover, linked selection, 3D, animation, sliders and interactive surfaces. Use Matplotlib for stable PNG/SVG/PDF render, regression testing and publication snapshots.
8. Avoid misleading encodings: truncated axes without reason, dual axes with unrelated scales, area/volume encoding for precise comparison, overplotting without density/alpha strategy, and unsupported causal arrows.
9. Preserve provenance in generated figures: source/ref, method, clock, evidence class and synthetic/real label when applicable.

## QA

Load `references/dual-render-qa.md` before outward publication. Load `references/provider-contract.md` for worker/runner invocation. Use `scripts/skill_contract.py` for deterministic resolution receipts.

## Forecast visuals

For predict-observe-learn loops, use `references/forecast-visuals.md`. Plot predictions and later actuals as distinct evidence classes and show forecast error/calibration as a first-class diagnostic.
