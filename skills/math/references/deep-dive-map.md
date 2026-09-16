# Math deep-dive map

## PCA
Classical covariance/correlation PCA -> robust, sparse, probabilistic, kernel and randomized PCA -> eigengap and Davis-Kahan perturbation -> temporal assignment/sign/congruence -> principal angles, Procrustes, projection/Grassmann distance -> streaming/subspace tracking/tensor PCA.

## Bradley-Terry
Likelihood/log-odds and reference constraints -> graph connectivity and finite-MLE conditions -> Hessian/Fisher information and uncertainty -> ties/context -> temporal BT -> hierarchical Bayesian/covariate-dependent BT.

## Confidence and uncertainty
90/95/99 fixed-horizon intervals -> t/Welch/Wilson/Fisher-z -> bootstrap percentile/basic/BCa and profile likelihood -> simultaneous bands -> confidence sequences, conformal prediction and selective inference. Keep confidence, prediction, tolerance and credible intervals distinct.

## Eigen/spectral methods
Trace/determinant/Rayleigh identities -> Weyl, Gershgorin and Davis-Kahan -> generalized eigenproblems -> repeated/near-repeated eigenvalues -> non-normality and pseudospectra -> MP/BBP and Tracy-Widom/free-probability frontiers.

## Matrix mathematics
Linear systems, inverses, projections and SVD -> QR/LU/Cholesky/Schur -> conditioning/backward error -> Kronecker/block/sparse structure -> matrix calculus/Jacobian/Hessian -> Stiefel/Grassmann/SPD manifolds -> randomized algorithms and low-rank completion.

## ANOVA and linear models
One-way decomposition -> Welch/two-way/interactions/repeated measures/ANCOVA -> contrasts and post-hoc inference -> Type I/II/III SS and unbalanced designs -> mixed/Bayesian/high-dimensional forms. Treat ANOVA as a linear-model family where useful.

## Covariance and multivariate
Covariance/correlation/partial correlation -> shrinkage and robust covariance -> Hotelling/MANOVA/CCA/LDA/QDA -> sparse precision/graphical models -> covariance manifold/Riemannian metrics.

## Regression / GLM
OLS -> robust SE/ridge/lasso/elastic net -> logistic/Poisson -> influence and leverage -> model selection/cross-validation -> GAM/quantile/hierarchical models. Check design-rank, residual, variance and link assumptions.

## Inference
Tests/p-values/effect sizes -> power and multiplicity/FDR -> permutation/exact tests -> equivalence/noninferiority -> sequential/e-value/selective inference. Never infer practical significance from p-value alone.

## Time series / state space
ACF/PACF, smoothing, ARIMA -> Kalman/state-space/change-point/spectral -> dynamic PCA/DMD/Koopman -> irregular/regime-switching/continuous-time SDE models.

## Calculus / dynamics
Derivative/integral/Jacobian/Hessian -> ODE/RK/stiffness/sensitivity -> fixed points/bifurcation/Lyapunov -> SDE/Fokker-Planck -> adjoint/differentiable simulation/control.

## Monte Carlo / resampling
IID bootstrap/permutation -> MC standard error and variance reduction -> QMC/importance/LHS -> rare events/nested MC -> particle/HMC/MLMC. Always distinguish Monte Carlo error from model/input uncertainty.

## Information theory
Entropy/KL/JS/MI -> conditional MI/HSIC/distance correlation -> redundancy/synergy -> transfer entropy -> information geometry. Dependence is not causality.

## Optimization / numerics
Gradient/Newton -> BFGS/coordinate/proximal/trust-region -> conditioning and regularization paths -> nonconvex/saddle/identifiability -> automatic differentiation/differentiable optimization.

## Probability / Bayesian
Distributions and Bayes -> posterior predictive -> hierarchy/calibration -> VI/GP/probabilistic programming. Inspect prior sensitivity, convergence and predictive calibration.

## Asymptotics / regime maps
Limits and nondimensional ratios -> CLT/delta method/perturbation -> p/n, effective rank, condition number, MP edge and eigengap joint maps -> phase transitions and universality.
