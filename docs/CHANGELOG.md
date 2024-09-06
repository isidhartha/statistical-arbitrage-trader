# Changelog

All notable changes are documented here.


### 2022-01-06
- test: add ADF stationarity test on synthetic spread


### 2022-01-20
- docs: add momentum signal formula to architecture.md


### 2022-01-28
- feat: add annualised CAGR and Sharpe ratio computation


### 2022-01-29
- style: fix ruff lint violations across modules


### 2022-02-01
- docs: add momentum signal formula to architecture.md


### 2022-02-04
- feat: implement reversal skip window for momentum strategy


### 2022-02-07
- docs: add Newton-Raphson convergence notes to API.md


### 2022-02-08
- fix: handle single-asset portfolio in ranking step


### 2022-02-09
- feat: add equity curve export as PNG chart


### 2022-02-12
- style: format all files with black


### 2022-02-15
- perf: cache rolling mean and std to avoid recomputation


### 2022-02-18
- test: verify put-call parity holds for sampled params


### 2022-02-27
- refactor: extract d1 d2 computation into shared helper


### 2022-03-02
- feat: implement Engle-Granger cointegration test screening


### 2022-03-04
- feat: implement long-short portfolio construction from rankings


### 2022-03-09
- feat: implement BacktestConfig dataclass with all parameters


### 2022-03-09
- style: normalise import ordering with isort


### 2022-03-11
- feat: implement synthetic cointegrated price data generator


### 2022-03-12
- refactor: extract plot configuration to named constants


### 2022-03-17
- docs: document Greeks interpretation and sign conventions


### 2022-03-17
- feat: implement option sensitivity sweep over spot range


### 2022-03-18
- test: add momentum signal computation unit tests


### 2022-03-23
- fix: fix stop-loss trigger for short positions


### 2022-03-26
- feat: add long-only mode disabling short portfolio leg


### 2022-03-29
- feat: implement long-short portfolio construction from rankings


### 2022-04-01
- style: normalise import ordering with isort


### 2022-04-03
- chore: add pre-commit config for black and ruff


### 2022-04-04
- feat: implement maximum drawdown calculation from equity curve


### 2022-04-05
- feat: add long-only mode disabling short portfolio leg


### 2022-04-12
- fix: resolve NaN spread values at start of rolling window


### 2022-04-15
- test: add momentum signal computation unit tests


### 2022-04-18
- chore: add pre-commit config for black and ruff


### 2022-04-19
- chore: update requirements.txt with pinned versions


### 2022-04-20
- refactor: extract d1 d2 computation into shared helper


### 2022-04-21
- docs: document cointegration theory in architecture.md


### 2022-04-21
- perf: reduce memory allocation in simulation loop


### 2022-04-22
- test: add cointegration screening test with synthetic data


### 2022-04-23
- test: add regression tests for all five Greeks


### 2022-04-26
- docs: add momentum signal formula to architecture.md


### 2022-05-03
- test: add regression tests for all five Greeks


### 2022-05-04
- docs: update setup instructions for scipy dependency


### 2022-05-05
- feat: add configurable transaction cost per strategy leg


### 2022-05-06
- test: add regression tests for all five Greeks


### 2022-05-15
- feat: implement OptionParams dataclass for clean pricing API


### 2022-05-17
- feat: implement rolling Z-score signal for mean-reversion


### 2022-05-24
- refactor: extract d1 d2 computation into shared helper


### 2022-05-26
- feat: add long-only mode disabling short portfolio leg


### 2022-05-28
- feat: implement OptionParams dataclass for clean pricing API


### 2022-05-30
- refactor: consolidate performance stats into compute_stats


### 2022-05-31
- fix: correct cointegration p-value threshold comparison


### 2022-06-02
- fix: handle single-asset portfolio in ranking step


### 2022-06-07
- docs: add momentum signal formula to architecture.md


### 2022-06-08
- docs: add example usage for implied volatility solver


### 2022-06-08
- style: fix ruff lint violations across modules


### 2022-06-09
- fix: resolve NaN spread values at start of rolling window


### 2022-06-11
- feat: implement BacktestConfig dataclass with all parameters


### 2022-06-13
- fix: correct cointegration p-value threshold comparison


### 2022-06-17
- docs: add momentum signal formula to architecture.md


### 2022-06-17
- test: add ADF stationarity test on synthetic spread


### 2022-06-21
- feat: add configurable transaction cost per strategy leg


### 2022-07-05
- refactor: separate pricing logic from Greeks computation


### 2022-07-05
- refactor: move synthetic data generators to data_utils


### 2022-07-05
- docs: document all BacktestConfig parameters in README


### 2022-07-05
- fix: correct theta formula for European put options


### 2022-07-18
- fix: fix momentum score when lookback exceeds available data


### 2022-07-19
- feat: add entry exit and stop-loss threshold configuration


### 2022-07-20
- fix: correct cointegration p-value threshold comparison


### 2022-07-23
- fix: resolve NaN spread values at start of rolling window


### 2022-07-24
- refactor: consolidate performance stats into compute_stats


### 2022-07-26
- test: add IV solver convergence test for ATM option


### 2022-07-27
- style: normalise import ordering with isort


### 2022-07-29
- feat: add 3-panel pair visualisation prices spread Z-score


### 2022-08-01
- feat: add entry exit and stop-loss threshold configuration


### 2022-08-01
- docs: add mathematical derivation notes for Black-Scholes


### 2022-08-05
- perf: vectorise momentum score computation with numpy


### 2022-08-09
- feat: add entry exit and stop-loss threshold configuration


### 2022-08-10
- docs: document all BacktestConfig parameters in README


### 2022-08-15
- perf: reduce memory allocation in simulation loop


### 2022-08-25
- test: add unit tests for Black-Scholes call price


### 2022-08-26
- chore: add pre-commit config for black and ruff


### 2022-09-01
- fix: resolve matplotlib backend error on headless systems


### 2022-09-02
- feat: implement rolling Z-score signal for mean-reversion


### 2022-09-12
- fix: fix max drawdown calculation at series start


### 2022-09-18
- fix: resolve NaN spread values at start of rolling window


### 2022-09-22
- fix: handle single-asset portfolio in ranking step


### 2022-09-24
- feat: add transaction cost modelling in basis points


### 2022-09-27
- refactor: separate pricing logic from Greeks computation


### 2022-10-03
- refactor: extract d1 d2 computation into shared helper


### 2022-10-04
- feat: implement long-short portfolio construction from rankings


### 2022-10-04
- feat: add equity curve export as PNG chart


### 2022-10-05
- feat: implement option sensitivity sweep over spot range


### 2022-10-07
- fix: correct theta formula for European put options


### 2022-10-07
- feat: add annualised CAGR and Sharpe ratio computation


### 2022-10-09
- feat: implement Black-Scholes pricing for European calls and puts


### 2022-10-17
- fix: handle sigma approaching zero in Black-Scholes formula


### 2022-10-19
- feat: add 3-panel pair visualisation prices spread Z-score


### 2022-10-24
- test: add ADF stationarity test on synthetic spread


### 2022-10-25
- feat: implement Black-Scholes pricing for European calls and puts


### 2022-10-27
- perf: reduce memory allocation in simulation loop


### 2022-11-03
- feat: implement long-short portfolio construction from rankings


### 2022-11-05
- feat: implement BacktestConfig dataclass with all parameters


### 2022-11-15
- fix: handle empty returns series in performance stats


### 2022-11-18
- feat: implement rolling Z-score signal for mean-reversion


### 2022-11-19
- fix: fix stop-loss trigger for short positions


### 2022-11-21
- docs: document all BacktestConfig parameters in README


### 2022-11-22
- test: add ADF stationarity test on synthetic spread


### 2022-11-23
- feat: implement long-short portfolio construction from rankings


### 2022-11-25
- feat: add configurable transaction cost per strategy leg


### 2022-11-25
- fix: fix momentum score when lookback exceeds available data


### 2022-11-29
- feat: add configurable transaction cost per strategy leg


### 2022-11-30
- chore: update requirements.txt with pinned versions


### 2022-12-06
- fix: fix stop-loss trigger for short positions


### 2022-12-08
- perf: vectorise momentum score computation with numpy


### 2022-12-14
- fix: resolve IV solver divergence for deep ITM options


### 2022-12-17
- fix: fix stop-loss trigger for short positions


### 2022-12-20
- docs: update setup instructions for scipy dependency


### 2022-12-23
- fix: correct cointegration p-value threshold comparison


### 2022-12-24
- feat: implement Newton-Raphson implied volatility solver


### 2022-12-31
- feat: implement option sensitivity sweep over spot range


### 2023-01-02
- refactor: extract plot configuration to named constants


### 2023-01-06
- docs: document cointegration theory in architecture.md


### 2023-01-09
- feat: implement long-short portfolio construction from rankings


### 2023-01-10
- fix: resolve IV solver divergence for deep ITM options


### 2023-01-17
- fix: correct sign convention for short leg PnL


### 2023-01-23
- feat: implement OptionParams dataclass for clean pricing API


### 2023-01-24
- fix: correct theta formula for European put options


### 2023-01-25
- fix: resolve matplotlib backend error on headless systems


### 2023-01-29
- feat: implement synthetic cointegrated price data generator


### 2023-02-07
- feat: add long-only mode disabling short portfolio leg


### 2023-02-08
- test: verify put-call parity holds for sampled params


### 2023-02-08
- style: normalise import ordering with isort


### 2023-02-13
- fix: correct theta formula for European put options


### 2023-02-14
- fix: handle zero vega edge case in Newton-Raphson loop


### 2023-02-14
- docs: add Newton-Raphson convergence notes to API.md


### 2023-02-25
- feat: add equity curve export as PNG chart


### 2023-02-26
- feat: add long-only mode disabling short portfolio leg


### 2023-03-11
- fix: correct cointegration p-value threshold comparison


### 2023-03-15
- fix: correct annualisation factor for different frequencies


### 2023-03-27
- fix: fix stop-loss trigger for short positions


### 2023-03-29
- feat: add entry exit and stop-loss threshold configuration


### 2023-04-01
- chore: add pre-commit config for black and ruff


### 2023-04-04
- fix: handle single-asset portfolio in ranking step


### 2023-04-09
- feat: implement Engle-Granger cointegration test screening


