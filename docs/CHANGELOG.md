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


### 2023-04-10
- refactor: extract d1 d2 computation into shared helper


### 2023-04-12
- fix: correct transaction cost application per portfolio leg


### 2023-04-13
- fix: handle zero vega edge case in Newton-Raphson loop


### 2023-04-14
- feat: implement cross-sectional momentum signal computation


### 2023-04-17
- docs: document all BacktestConfig parameters in README


### 2023-04-17
- feat: implement OptionParams dataclass for clean pricing API


### 2023-04-18
- feat: implement maximum drawdown calculation from equity curve


### 2023-04-21
- chore: pin scipy to 1.11 for norm API compatibility


### 2023-04-29
- fix: handle sigma approaching zero in Black-Scholes formula


### 2023-05-01
- feat: implement Engle-Granger cointegration test screening


### 2023-05-04
- refactor: consolidate performance stats into compute_stats


### 2023-05-12
- fix: handle zero vega edge case in Newton-Raphson loop


### 2023-05-12
- feat: add entry exit and stop-loss threshold configuration


### 2023-05-17
- fix: handle single-asset portfolio in ranking step


### 2023-05-18
- perf: cache rolling mean and std to avoid recomputation


### 2023-05-30
- chore: add .gitignore entries for PNG output files


### 2023-05-31
- feat: implement synthetic cointegrated price data generator


### 2023-06-01
- fix: handle zero vega edge case in Newton-Raphson loop


### 2023-06-07
- feat: implement long-short portfolio construction from rankings


### 2023-06-14
- fix: handle empty returns series in performance stats


### 2023-06-19
- feat: add full Greeks calculator delta gamma vega theta rho


### 2023-06-30
- feat: implement reversal skip window for momentum strategy


### 2023-07-02
- docs: update setup instructions for scipy dependency


### 2023-07-03
- style: format all files with black


### 2023-07-05
- refactor: move synthetic data generators to data_utils


### 2023-07-07
- chore: pin scipy to 1.11 for norm API compatibility


### 2023-07-13
- fix: fix stop-loss trigger for short positions


### 2023-07-28
- feat: add equity curve export as PNG chart


### 2023-08-01
- docs: add Newton-Raphson convergence notes to API.md


### 2023-08-04
- chore: update requirements.txt with pinned versions


### 2023-08-04
- perf: vectorise momentum score computation with numpy


### 2023-08-07
- feat: implement ADF stationarity test on spread series


### 2023-08-14
- refactor: rename position variable for clarity in backtest


### 2023-08-27
- perf: cache rolling mean and std to avoid recomputation


### 2023-08-28
- chore: add .gitignore entries for PNG output files


### 2023-08-28
- chore: update requirements.txt with pinned versions


### 2023-09-09
- fix: resolve IV solver divergence for deep ITM options


### 2023-09-10
- feat: add OLS hedge ratio estimation for spread construction


### 2023-10-01
- chore: update requirements.txt with pinned versions


### 2023-10-09
- refactor: split large backtest loop into focused helpers


### 2023-10-10
- feat: add transaction cost modelling in basis points


### 2023-10-19
- test: add cointegration screening test with synthetic data


### 2023-10-26
- feat: add entry exit and stop-loss threshold configuration


### 2023-10-27
- refactor: separate pricing logic from Greeks computation


### 2023-10-30
- feat: implement OptionParams dataclass for clean pricing API


### 2023-11-01
- feat: add 6-panel sensitivity dashboard with matplotlib


### 2023-11-06
- fix: handle single-asset portfolio in ranking step


### 2023-11-07
- feat: add OLS hedge ratio estimation for spread construction


### 2023-11-27
- fix: fix momentum score when lookback exceeds available data


### 2023-12-01
- test: add IV solver convergence test for ATM option


### 2023-12-06
- test: add unit tests for Black-Scholes call price


### 2023-12-09
- test: add ADF stationarity test on synthetic spread


### 2023-12-11
- fix: fix stop-loss trigger for short positions


### 2023-12-14
- feat: implement ADF stationarity test on spread series


### 2023-12-14
- fix: correct annualisation factor for different frequencies


### 2023-12-18
- fix: handle sigma approaching zero in Black-Scholes formula


### 2023-12-22
- feat: implement Engle-Granger cointegration test screening


### 2023-12-27
- docs: update setup instructions for scipy dependency


### 2023-12-28
- feat: add entry exit and stop-loss threshold configuration


### 2023-12-29
- docs: document all BacktestConfig parameters in README


### 2023-12-30
- perf: reduce memory allocation in simulation loop


### 2024-01-01
- feat: add annualised CAGR and Sharpe ratio computation


### 2024-01-01
- feat: add long-only mode disabling short portfolio leg


### 2024-01-08
- test: add momentum signal computation unit tests


### 2024-01-11
- fix: correct transaction cost application per portfolio leg


### 2024-01-13
- feat: add 6-panel sensitivity dashboard with matplotlib


### 2024-01-18
- docs: add Newton-Raphson convergence notes to API.md


### 2024-01-21
- refactor: rename position variable for clarity in backtest


### 2024-01-23
- feat: implement ADF stationarity test on spread series


### 2024-02-01
- docs: update setup instructions for scipy dependency


### 2024-02-09
- feat: implement reversal skip window for momentum strategy


### 2024-02-19
- docs: add momentum signal formula to architecture.md


### 2024-02-22
- docs: update setup instructions for scipy dependency


### 2024-02-23
- fix: correct sign convention for short leg PnL


### 2024-02-23
- docs: document Greeks interpretation and sign conventions


### 2024-02-26
- style: normalise import ordering with isort


### 2024-03-08
- fix: handle empty returns series in performance stats


### 2024-03-11
- feat: add transaction cost modelling in basis points


### 2024-03-13
- feat: implement rolling Z-score signal for mean-reversion


### 2024-03-17
- fix: resolve IV solver divergence for deep ITM options


### 2024-03-23
- perf: vectorise momentum score computation with numpy


### 2024-03-24
- feat: implement option sensitivity sweep over spot range


### 2024-03-27
- fix: resolve IV solver divergence for deep ITM options


### 2024-03-27
- fix: fix momentum score when lookback exceeds available data


### 2024-03-28
- perf: reduce memory allocation in simulation loop


### 2024-04-01
- feat: add PairsConfig dataclass for pairs trading settings


### 2024-04-03
- feat: implement rolling Z-score signal for mean-reversion


### 2024-04-10
- fix: correct cointegration p-value threshold comparison


### 2024-04-10
- fix: resolve matplotlib backend error on headless systems


### 2024-04-18
- style: normalise import ordering with isort


### 2024-04-19
- fix: correct transaction cost application per portfolio leg


### 2024-04-19
- feat: implement long-short portfolio construction from rankings


### 2024-04-20
- fix: correct transaction cost application per portfolio leg


### 2024-04-26
- test: add cointegration screening test with synthetic data


### 2024-05-01
- fix: fix momentum score when lookback exceeds available data


### 2024-05-06
- fix: fix max drawdown calculation at series start


### 2024-05-07
- feat: add configurable lookback and holding period windows


### 2024-05-07
- fix: correct theta formula for European put options


### 2024-05-13
- fix: fix stop-loss trigger for short positions


### 2024-05-16
- feat: implement option sensitivity sweep over spot range


### 2024-05-22
- fix: correct transaction cost application per portfolio leg


### 2024-05-23
- feat: add annualised CAGR and Sharpe ratio computation


### 2024-05-23
- perf: vectorise momentum score computation with numpy


### 2024-05-30
- fix: correct annualisation factor for different frequencies


### 2024-06-07
- feat: add transaction cost modelling in basis points


### 2024-06-09
- feat: implement cross-sectional momentum signal computation


### 2024-06-10
- chore: pin scipy to 1.11 for norm API compatibility


### 2024-06-12
- fix: correct sign convention for short leg PnL


### 2024-06-13
- fix: fix stop-loss trigger for short positions


### 2024-06-13
- feat: add configurable lookback and holding period windows


### 2024-06-16
- fix: handle identical assets in cointegration screener


### 2024-06-23
- test: add ADF stationarity test on synthetic spread


### 2024-06-30
- fix: resolve NaN spread values at start of rolling window


### 2024-07-02
- fix: correct cointegration p-value threshold comparison


### 2024-07-04
- refactor: consolidate performance stats into compute_stats


### 2024-07-05
- fix: handle single-asset portfolio in ranking step


### 2024-07-06
- fix: fix max drawdown calculation at series start


### 2024-07-12
- docs: add example usage for implied volatility solver


### 2024-07-16
- fix: correct theta formula for European put options


### 2024-07-19
- test: add regression tests for all five Greeks


### 2024-07-19
- refactor: consolidate performance stats into compute_stats


### 2024-07-22
- docs: update setup instructions for scipy dependency


### 2024-08-01
- test: add ADF stationarity test on synthetic spread


### 2024-08-02
- refactor: move synthetic data generators to data_utils


### 2024-08-04
- fix: correct sign convention for short leg PnL


### 2024-08-05
- feat: add long-only mode disabling short portfolio leg


### 2024-08-06
- fix: correct cointegration p-value threshold comparison


### 2024-08-07
- fix: handle identical assets in cointegration screener


### 2024-08-13
- style: fix ruff lint violations across modules


### 2024-08-14
- fix: correct theta formula for European put options


### 2024-08-21
- chore: add pre-commit config for black and ruff


### 2024-08-28
- docs: add example usage for implied volatility solver


### 2024-09-11
- test: verify put-call parity holds for sampled params


### 2024-09-14
- fix: handle single-asset portfolio in ranking step


### 2024-09-22
- fix: handle sigma approaching zero in Black-Scholes formula


### 2024-09-23
- refactor: consolidate performance stats into compute_stats


### 2024-09-28
- feat: add equity curve export as PNG chart


### 2024-10-01
- feat: implement option sensitivity sweep over spot range


### 2024-10-02
- fix: resolve NaN spread values at start of rolling window


### 2024-10-04
- refactor: move synthetic data generators to data_utils


### 2024-10-06
- perf: cache rolling mean and std to avoid recomputation


### 2024-10-07
- feat: add OLS hedge ratio estimation for spread construction


### 2024-10-08
- docs: update setup instructions for scipy dependency


### 2024-10-12
- fix: fix max drawdown calculation at series start


### 2024-10-15
- test: add unit tests for Black-Scholes call price


### 2024-10-16
- feat: implement maximum drawdown calculation from equity curve


### 2024-10-23
- fix: resolve matplotlib backend error on headless systems


### 2024-10-24
- test: add IV solver convergence test for ATM option


### 2024-10-26
- refactor: extract d1 d2 computation into shared helper


### 2024-10-31
- fix: resolve IV solver divergence for deep ITM options


### 2024-11-05
- chore: update requirements.txt with pinned versions


### 2024-11-14
- feat: implement rolling Z-score signal for mean-reversion


### 2024-11-22
- fix: resolve NaN spread values at start of rolling window


### 2024-11-22
- feat: implement Newton-Raphson implied volatility solver


### 2024-11-26
- fix: handle empty returns series in performance stats


### 2024-12-02
- docs: document Greeks interpretation and sign conventions


### 2024-12-03
- fix: resolve NaN spread values at start of rolling window


### 2024-12-11
- feat: implement long-short portfolio construction from rankings


### 2024-12-12
- feat: add equity curve export as PNG chart


### 2024-12-16
- refactor: move synthetic data generators to data_utils


### 2024-12-18
- test: add IV solver convergence test for ATM option


### 2024-12-19
- feat: add equity curve export as PNG chart


### 2025-01-01
- fix: resolve matplotlib backend error on headless systems


### 2025-01-03
- feat: implement Newton-Raphson implied volatility solver


### 2025-01-06
- feat: add OLS hedge ratio estimation for spread construction


### 2025-01-10
- test: add ADF stationarity test on synthetic spread


### 2025-01-15
- fix: handle identical assets in cointegration screener


### 2025-01-20
- docs: add example usage for implied volatility solver


### 2025-01-20
- fix: handle single-asset portfolio in ranking step


### 2025-01-21
- feat: add configurable lookback and holding period windows


### 2025-01-22
- chore: update requirements.txt with pinned versions


### 2025-01-23
- test: add regression tests for all five Greeks


### 2025-01-25
- chore: pin scipy to 1.11 for norm API compatibility


### 2025-01-28
- style: format all files with black


### 2025-01-28
- fix: handle empty returns series in performance stats


### 2025-02-09
- feat: implement rolling Z-score signal for mean-reversion


### 2025-02-11
- fix: handle sigma approaching zero in Black-Scholes formula


### 2025-02-11
- test: add ADF stationarity test on synthetic spread


### 2025-02-13
- feat: add PairsConfig dataclass for pairs trading settings


### 2025-02-14
- fix: fix momentum score when lookback exceeds available data


### 2025-02-16
- refactor: consolidate performance stats into compute_stats


### 2025-02-19
- fix: correct cointegration p-value threshold comparison


### 2025-02-19
- feat: implement OptionParams dataclass for clean pricing API


### 2025-02-27
- feat: implement Newton-Raphson implied volatility solver


### 2025-03-02
- fix: handle single-asset portfolio in ranking step


### 2025-03-02
- feat: add transaction cost modelling in basis points


### 2025-03-07
- feat: implement maximum drawdown calculation from equity curve


### 2025-03-10
- feat: implement cross-sectional momentum signal computation


### 2025-03-10
- feat: implement ADF stationarity test on spread series


