# Math x Plots N+2 loop

At each ordered pulse N, bind the mathematical forecast and visual evidence in one receipt:
- actual_N;
- prediction_N_plus_1;
- prediction_N_plus_2;
- estimator_state_before;
- assumptions and uncertainty;
- when observed: actual_N_plus_1, error metrics, estimator_state_after;
- rolled predictions for N+2 and N+3.

The visual layer should include actual-vs-forecast, error evolution and calibration/coverage when applicable. The mathematical layer owns the estimator and scoring rule. Do not let the rendering layer update the model.
