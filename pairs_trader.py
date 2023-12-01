"""
Statistical Arbitrage Trader
Pairs trading strategy backtester using cointegration and Z-score signals.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint, adfuller
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from dataclasses import dataclass
from itertools import combinations
from typing import Tuple, List


@dataclass
class PairsConfig:
    lookback_window: int = 60      # days for rolling spread mean/std
    entry_z: float = 2.0           # Z-score to open a position
    exit_z: float = 0.5            # Z-score to close a position
    stop_loss_z: float = 4.0       # Z-score stop-loss
    transaction_cost_bps: float = 5.0


def load_prices(path: str = "data/prices.csv") -> pd.DataFrame:
    try:
        return pd.read_csv(path, index_col=0, parse_dates=True)
    except FileNotFoundError:
        print("[INFO] No data file found — using synthetic correlated pairs.")
        return _synthetic_cointegrated_prices()


def _synthetic_cointegrated_prices(n: int = 1000) -> pd.DataFrame:
    rng = np.random.default_rng(7)
    common = np.cumsum(rng.normal(0, 1, n))
    noise_a = rng.normal(0, 0.5, n)
    noise_b = rng.normal(0, 0.5, n)
    # B cointegrated with A: B = 1.5*A + noise
    A = 100 + common + noise_a
    B = 100 + 1.5 * common + noise_b
    C = 100 + np.cumsum(rng.normal(0, 1, n))   # unrelated asset
    idx = pd.bdate_range("2020-01-01", periods=n)
    return pd.DataFrame({"ASSET_A": A, "ASSET_B": B, "ASSET_C": C}, index=idx)


def test_cointegration(prices: pd.DataFrame, p_threshold: float = 0.05) -> List[Tuple]:
    pairs = []
    cols = prices.columns.tolist()
    for a, b in combinations(cols, 2):
        _, pval, _ = coint(prices[a], prices[b])
        if pval < p_threshold:
            pairs.append((a, b, pval))
    pairs.sort(key=lambda x: x[2])
    return pairs


def compute_spread(series_a: pd.Series, series_b: pd.Series) -> Tuple[pd.Series, float]:
    """OLS hedge ratio: spread = A - beta * B"""
    model = OLS(series_a, add_constant(series_b)).fit()
    beta = model.params.iloc[1]
    spread = series_a - beta * series_b
    return spread, beta


def compute_zscore(spread: pd.Series, window: int) -> pd.Series:
    mean = spread.rolling(window).mean()
    std = spread.rolling(window).std()
    return (spread - mean) / std


def backtest_pair(
    prices: pd.DataFrame,
    asset_a: str,
    asset_b: str,
    cfg: PairsConfig,
) -> pd.Series:
    spread, beta = compute_spread(prices[asset_a], prices[asset_b])
    zscore = compute_zscore(spread, cfg.lookback_window)

    position = 0   # +1 long A/short B, -1 short A/long B
    daily_pnl = []
    dates = []
    tc = cfg.transaction_cost_bps / 10000

    for i in range(cfg.lookback_window + 1, len(prices)):
        date = prices.index[i]
        z = zscore.iloc[i]

        ret_a = prices[asset_a].pct_change().iloc[i]
        ret_b = prices[asset_b].pct_change().iloc[i]

        if np.isnan(z):
            daily_pnl.append(0)
            dates.append(date)
            continue

        prev_position = position

        if position == 0:
            if z < -cfg.entry_z:
                position = 1    # long A, short B
            elif z > cfg.entry_z:
                position = -1   # short A, long B
        elif position == 1:
            if z > -cfg.exit_z or z > cfg.stop_loss_z:
                position = 0
        elif position == -1:
            if z < cfg.exit_z or z < -cfg.stop_loss_z:
                position = 0

        # PnL: long A - beta * short B (normalised)
        pnl = position * (ret_a - beta * ret_b)
        trade_cost = abs(position - prev_position) * tc
        daily_pnl.append(pnl - trade_cost)
        dates.append(date)

    return pd.Series(daily_pnl, index=dates, name=f"{asset_a}/{asset_b}")


def run_adf(spread: pd.Series) -> dict:
    result = adfuller(spread.dropna())
    return {"ADF Statistic": result[0], "p-value": result[1]}


def plot_pair(prices: pd.DataFrame, asset_a: str, asset_b: str, cfg: PairsConfig):
    spread, _ = compute_spread(prices[asset_a], prices[asset_b])
    zscore = compute_zscore(spread, cfg.lookback_window)

    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    fig.suptitle(f"Pairs Analysis: {asset_a} vs {asset_b}")

    prices[[asset_a, asset_b]].plot(ax=axes[0], title="Price Series")
    spread.plot(ax=axes[1], title="Spread", color="purple")
    zscore.plot(ax=axes[2], title="Z-Score", color="teal")
    for thresh in [cfg.entry_z, -cfg.entry_z, cfg.exit_z, -cfg.exit_z]:
        axes[2].axhline(thresh, linestyle="--", alpha=0.5)

    for ax in axes:
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"pair_{asset_a}_{asset_b}.png", dpi=150)
    print(f"Saved pair_{asset_a}_{asset_b}.png")
    plt.show()


if __name__ == "__main__":
    cfg = PairsConfig()
    prices = load_prices()

    print("Testing for cointegrated pairs...")
    pairs = test_cointegration(prices)

    if not pairs:
        print("No cointegrated pairs found at p<0.05.")
    else:
        print(f"Found {len(pairs)} cointegrated pair(s):")
        for a, b, pval in pairs:
            print(f"  {a} / {b}  (p={pval:.4f})")

        best_a, best_b, _ = pairs[0]
        returns = backtest_pair(prices, best_a, best_b, cfg)
        cum = (1 + returns).cumprod()
        total = cum.iloc[-1] - 1
        ann_ret = (1 + total) ** (252 / len(returns)) - 1
        vol = returns.std() * np.sqrt(252)
        sharpe = ann_ret / vol if vol else 0

        print(f"\nBacktest: {best_a}/{best_b}")
        print(f"  Total Return : {total:.2%}")
        print(f"  Ann. Return  : {ann_ret:.2%}")
        print(f"  Volatility   : {vol:.2%}")
        print(f"  Sharpe Ratio : {sharpe:.2f}")

        spread, _ = compute_spread(prices[best_a], prices[best_b])
        adf = run_adf(spread)
        print(f"  ADF p-value  : {adf['p-value']:.4f}")

        plot_pair(prices, best_a, best_b, cfg)
