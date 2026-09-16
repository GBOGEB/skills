# Visual grammar

## Comparison
Bar/dot/lollipop for discrete categories; line only when x-order has semantic continuity. Waterfall for additive deltas. Forest/interval plot for estimates with uncertainty.

## Distribution
Histogram/ECDF/KDE for one distribution; box/violin/raincloud for grouped distributions. Show sample size and avoid implying density precision unsupported by n.

## Relationship
Scatter for paired numeric observations; hexbin/density contours for heavy overlap; line/fitted band for modeled relationship. Pair plot only when the dimensionality remains readable.

## Matrix and field
Heatmap for matrix/intensity; contour for level sets; surface for z=f(x,y); mesh when topology/triangulation is meaningful. Label whether a matrix is covariance, correlation, distance, adjacency, information, confusion, transition, etc.

## Geometry and 3D
Use `Scatter3d` for points/vectors, `Surface` for gridded response, `Mesh3d` for triangulated geometry, cone/streamtube for vector fields. Provide 2D projections or static snapshots when 3D occlusion hides structure.

## Flow/topology
Sankey for conserved or approximately additive flow. Network/dependency graph for topology; edge width/direction must have declared semantics. Chord/radial relationship diagrams are supplemental, not a substitute for a precise matrix when exact comparison matters.

## Cyclic/radial
Polar/radar for genuinely angular/cyclic data or compact fingerprints. Do not use radar charts for precise ranking across many variables unless a table or dot plot accompanies it.

## Temporal/state evolution
Line/step/area for ordered evolution. Animation or slider may use wall time, pulse, wave, PR, release, DMAIC iteration or model version. Declare the clock and spacing semantics.

## Uncertainty
Error bars, ribbons, fan charts, bootstrap clouds, confidence ellipses/ellipsoids and posterior bands. State whether intervals are confidence, credible, prediction, tolerance or empirical quantiles.
