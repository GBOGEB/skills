# Forecast and actual visual grammar

For rolling N+2 work, distinguish forecasts from actuals visually and semantically.

Preferred views:
- actual trace plus N+1/N+2 forecast markers or fan band;
- forecast-vs-actual parity scatter with 1:1 reference;
- signed/absolute error by pulse;
- rolling MAE/RMSE or Brier score;
- interval coverage strip and interval width trace;
- calibration/reliability diagram for probabilistic forecasts;
- transition heatmap for categorical/ordinal states.

Never connect unobserved future points as if they were actual measurements. Preserve the clock label (time, wave, PR, pulse, cycle, version) and whether spacing is metric or ordinal.
