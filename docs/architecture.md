# Architecture — Statistical Arbitrage Trader

## Overview

Statistical arbitrage exploits the tendency of historically cointegrated asset pairs to mean-revert toward a long-run equilibrium. This backtester implements the full pairs trading pipeline: universe screening via cointegration tests, hedge ratio estimation, spread construction, Z-score signal generation, and a rule-based trading state machine with risk controls.

## Cointegration Theory

Two individually non-stationary (I(1)) price series A and B are cointegrated if a linear combination `A - beta * B` is stationary (I(0)). Economic intuition: if two assets share common fundamental drivers (e.g., two banks, two oil majors), their prices should not drift arbitrarily far apart in the long run.

The Engle-Granger two-step method implemented here:

1. **Step 1 — Estimate the hedge ratio**: Regress A on B using OLS: `A = alpha + beta * B + epsilon`. The OLS coefficient `beta` is the hedge ratio.
2. **Step 2 — Test residual stationarity**: Apply the Augmented Dickey-Fuller test to the residual series `epsilon`. If the ADF test rejects the unit root hypothesis (p-value below a threshold, typically 0.05), the pair is declared cointegrated.

`statsmodels.tsa.stattools.coint()` performs both steps and returns the ADF test statistic and p-value.

## Spread Construction

Given hedge ratio `beta` estimated from OLS, the spread at time `t` is:

```
spread_t = A_t - beta * B_t
```

A stationary spread oscillates around a stable mean, creating the mean-reversion opportunity the strategy exploits.

## Z-Score Signal and State Machine

The Z-score normalises the spread relative to its recent history:

```
z_t = (spread_t - rolling_mean_t) / rolling_std_t
```

where rolling mean and standard deviation are computed over a configurable `lookback_window`. This makes the signal scale-invariant and directly comparable across pairs.

The trading state machine has four states:

```
FLAT ──[z < -entry_z]──► LONG_SPREAD  ──[|z| < exit_z]──► FLAT
     ──[z > +entry_z]──► SHORT_SPREAD ──[|z| < exit_z]──► FLAT
LONG_SPREAD  ──[z < -stop_z]──► FLAT (stop-loss)
SHORT_SPREAD ──[z > +stop_z]──► FLAT (stop-loss)
```

| Signal | Action |
|---|---|
| `z < -entry_z` | Long A, short B (spread expected to rise) |
| `z > +entry_z` | Short A, long B (spread expected to fall) |
| `\|z\| < exit_z` | Close position (spread has mean-reverted) |
| `\|z\| > stop_z` | Stop-loss exit (spread diverging further) |

## Backtest Loop Design

The backtest iterates day-by-day over the price series. At each step:

1. Compute the current spread value using the pre-estimated hedge ratio.
2. Compute the rolling Z-score.
3. Evaluate the state machine transition rules.
4. If a position exists, compute daily PnL: `pnl_t = position * (ret_A_t - beta * ret_B_t)`.
5. On entry or exit, deduct transaction costs: `cost = cost_bps / 10000 * notional`.

Daily PnL is accumulated into a return series, which is then passed to `compute_stats()` for performance metrics.

## Extension Points

- **Dynamic hedge ratio**: Replace the static OLS `beta` with a Kalman filter that updates the hedge ratio as new price data arrives, adapting to structural changes in the relationship.
- **Johansen test**: The Engle-Granger test is limited to two-asset pairs. The Johansen cointegration test supports baskets of three or more assets and identifies multiple cointegrating vectors simultaneously.
- **Regime filtering**: Use a hidden Markov model or trend indicator to disable trading during trending regimes when pairs are more likely to diverge further rather than mean-revert.
- **Walk-forward validation**: Re-estimate cointegration and hedge ratio on a rolling training window to avoid the in-sample look-ahead bias inherent in static parameter estimation.
