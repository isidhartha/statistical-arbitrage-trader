# Module API — Statistical Arbitrage Trader

`pairs_trader.py` exposes a functional API for cointegration testing, spread construction, signal generation, backtesting, and visualisation.

---

## `load_prices(data_path: str | None = None) -> pd.DataFrame`

Loads a wide-format price matrix from CSV. Generates a synthetic cointegrated dataset if the file is not found.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `data_path` | `str \| None` | `None` | Path to the price CSV. Falls back to the `DATA_PATH` environment variable, then to synthetic data generation. |

**Returns:** A `pd.DataFrame` with a `pd.DatetimeIndex` and ticker symbols as columns.

**Example:**

```python
from pairs_trader import load_prices

prices = load_prices("./data/prices.csv")
```

---

## `test_cointegration(prices: pd.DataFrame, p_threshold: float = 0.05) -> list[tuple]`

Screens all asset pairs in the universe for cointegration using the Engle-Granger two-step method.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `prices` | `pd.DataFrame` | — | Wide-format price matrix |
| `p_threshold` | `float` | `0.05` | Maximum p-value to consider a pair cointegrated |

**Returns:** A list of tuples `(asset_a, asset_b, p_value)`, sorted by ascending p-value. Only pairs with `p_value <= p_threshold` are included.

**Example:**

```python
from pairs_trader import load_prices, test_cointegration

prices = load_prices()
pairs = test_cointegration(prices, p_threshold=0.05)
for a, b, p in pairs:
    print(f"{a}/{b}: p = {p:.4f}")
```

---

## `compute_spread(series_a: pd.Series, series_b: pd.Series) -> tuple[pd.Series, float]`

Estimates the hedge ratio via OLS regression and constructs the spread series.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `series_a` | `pd.Series` | Price series for asset A (dependent variable) |
| `series_b` | `pd.Series` | Price series for asset B (independent variable) |

**Returns:** A tuple `(spread, beta)` where:
- `spread` is a `pd.Series` of `A_t - beta * B_t`
- `beta` is the OLS hedge ratio (float)

**Example:**

```python
from pairs_trader import load_prices, compute_spread

prices = load_prices()
spread, beta = compute_spread(prices["ASSET_A"], prices["ASSET_B"])
print(f"Hedge ratio: {beta:.4f}")
```

---

## `compute_zscore(spread: pd.Series, window: int = 30) -> pd.Series`

Computes the rolling Z-score of the spread.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `spread` | `pd.Series` | — | Spread series from `compute_spread()` |
| `window` | `int` | `30` | Rolling window size in periods |

**Returns:** A `pd.Series` of Z-scores. The first `window - 1` values are `NaN`.

**Example:**

```python
from pairs_trader import compute_zscore

zscore = compute_zscore(spread, window=30)
```

---

## `backtest_pair(prices: pd.DataFrame, asset_a: str, asset_b: str, entry_z: float = 2.0, exit_z: float = 0.5, stop_z: float = 3.5, window: int = 30, cost_bps: float = 5.0) -> pd.Series`

Runs the full backtest simulation for a single asset pair.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `prices` | `pd.DataFrame` | — | Wide-format price matrix |
| `asset_a` | `str` | — | Ticker for asset A |
| `asset_b` | `str` | — | Ticker for asset B |
| `entry_z` | `float` | `2.0` | Z-score threshold to enter a trade |
| `exit_z` | `float` | `0.5` | Z-score threshold to exit a trade |
| `stop_z` | `float` | `3.5` | Z-score threshold for stop-loss exit |
| `window` | `int` | `30` | Rolling window for Z-score computation |
| `cost_bps` | `float` | `5.0` | One-way transaction cost in basis points |

**Returns:** A `pd.Series` of daily strategy returns.

---

## `run_adf(spread: pd.Series) -> dict`

Runs the Augmented Dickey-Fuller test on the spread to confirm stationarity.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `spread` | `pd.Series` | Spread series from `compute_spread()` |

**Returns:**

```python
{
    "adf_statistic": float,   # ADF test statistic (more negative = more stationary)
    "p_value": float,         # p-value of the test
    "used_lag": int,          # Lag order selected by the ADF test
    "is_stationary": bool,    # True if p_value < 0.05
}
```

---

## `plot_pair(prices: pd.DataFrame, asset_a: str, asset_b: str, spread: pd.Series, zscore: pd.Series, output_dir: str = "./output") -> None`

Generates and saves a 3-panel visualisation of the pair.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `prices` | `pd.DataFrame` | Wide-format price matrix (for the normalised price chart) |
| `asset_a` | `str` | Ticker for asset A |
| `asset_b` | `str` | Ticker for asset B |
| `spread` | `pd.Series` | Spread series |
| `zscore` | `pd.Series` | Z-score series |
| `output_dir` | `str` | Directory to save the PNG (default: `./output`) |

**Side effects:** Saves `{output_dir}/pair_{asset_a}_{asset_b}.png` with three panels: normalised price series, spread with rolling mean bands, and Z-score with entry/exit threshold lines.
