# Plotly + Matplotlib dual-render QA

For governed outputs, prefer one semantic specification feeding two renderers.

Plotly responsibilities:
- hover details and provenance;
- animation/frames/sliders;
- 3D camera rotation;
- surface/mesh inspection;
- linked interactive exploration;
- self-contained HTML when required.

Matplotlib responsibilities:
- deterministic PNG/SVG/PDF snapshots;
- publication sizing and typography checks;
- CI image/hash or perceptual-diff baselines where appropriate;
- fallback when interactive runtime is unavailable.

Cross-render checks:
- same source data and transform;
- same axis variables, units and limits unless explicitly documented;
- same uncertainty/threshold semantics;
- same evidence/synthetic labels;
- no hidden filtering in one renderer;
- static snapshot captures the principal interactive finding.
