# Temporal, 3D and surface rules

A temporal frame may be indexed by time, sample, pulse, wave, PR, release, mission step, DMAIC iteration or model version. Declare the clock and whether spacing is metric or merely ordinal.

For temporal PCA, never animate raw signs/components across independent fits before alignment. Prefer:
- eigenvalue surface: component x clock -> eigenvalue;
- loading heatmap: variable x component with clock slider;
- aligned PC1-PC3 score/loadings animation;
- principal-angle or Grassmann-distance trace;
- Procrustes displacement vectors;
- regime surface with eigengap/stability overlays.

For generic 3D:
- use z only for a third mathematical variable;
- include 2D projections when occlusion matters;
- surface requires gridded response or an explicit interpolation model;
- mesh requires meaningful triangulation/topology;
- camera perspective must not be the only way to see the conclusion.
