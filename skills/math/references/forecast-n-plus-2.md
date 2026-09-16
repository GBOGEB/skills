# Rolling N+2 forecast-observe-learn loop

Use a rolling horizon when work is executed in waves, pulses, PRs, DMAIC cycles, model versions or other ordered clocks.

At pulse N:
1. record actual state and measured outputs for N;
2. predict bounded outcomes for N+1 and N+2 before observing them;
3. store prediction timestamp, source ref, estimator/rule, uncertainty or categorical confidence class, and assumptions;
4. when N+1 becomes actual, compute forecast error using a metric appropriate to the variable;
5. update calibration parameters only from observed error, never by rewriting the historical prediction;
6. roll the horizon forward and emit predictions for N+2 and N+3.

Recommended metrics:
- continuous: signed error, absolute error, squared error, MAPE only when denominator is safely nonzero, interval coverage and width;
- binary/categorical: Brier score or log score when calibrated probabilities exist; otherwise confusion counts and hit rate;
- ordinal/state: absolute step error or transition-matrix score;
- multivariate: Mahalanobis error only with a justified covariance model; otherwise per-dimension errors plus norm.

Keep `prediction` and `actual` immutable once recorded. Learning updates the estimator state, not history.
