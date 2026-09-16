# Regime and temporal mathematics

Use an ordered state clock, not only wall time. Valid clocks include seconds, sample index, pulse, wave, PR, release, DMAIC cycle, mission step, model version or another monotone state label.

For repeated PCA/eigenspace fits, compare in this order where applicable:
1. eigenvalues and eigengaps;
2. component assignment;
3. sign/orientation alignment;
4. loading congruence;
5. principal angles/canonical correlations;
6. orthogonal Procrustes alignment;
7. projection-matrix or Grassmann/geodesic distance;
8. aligned effect/loading comparison;
9. finite differences of distance/angle for velocity, acceleration and curvature only when the clock spacing is meaningful.

For regime maps, prefer dimensionless or scale-normalized axes. Useful joint indicators include `p/n`, effective-rank/p, condition number, eigengap ratio, MP-edge exceedance, signal-to-noise, leverage/outlier fraction and bootstrap congruence.
