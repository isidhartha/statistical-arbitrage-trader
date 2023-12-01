# Contributing to Statistical Arbitrage Trader

## Getting Started

1. Fork and clone the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Set up environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run `python pairs_trader.py` to verify
5. Lint: `ruff check .` and `black .`
6. Open a Pull Request

## Ideas for Contribution

- Johansen cointegration test (supports >2 assets)
- Kalman filter for dynamic hedge ratio
- Regime detection (switch off in trending markets)
- Live trading via broker API
