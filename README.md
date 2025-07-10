# Quant-Backtrader

This is a **learning project based on Backtrader**, aiming to help beginners build a solid foundation in quantitative backtesting. It includes implementations of common technical strategies, result analysis, chart visualization, and basic parameter optimization.

---

## Project Structure

```
quant-backtrader/
├── backtests/                  # Backtest scripts for each strategy
│   ├── backtest_sma.py
│   ├── backtest_rsi.py
│   └── ...
├── data/                       # Sample CSV data files
│   ├── sample_data.csv
│   └── maotai_sample.csv
├── docs/                       # Backtest reports and result CSVs
│   ├── sma_crossover_report.md
│   └── result_sma_opt.csv
├── images/                     # Generated charts
│   ├── backtest_sma_result.png
│   └── ...
├── notebooks/                  # Educational Jupyter notebooks
│   └── backtrader_tutorial.ipynb
├── strategies/                 # Strategy class implementations
│   ├── bt_sma_strategy.py
│   ├── bt_rsi_strategy.py
│   └── ...
├── utils/                      # Utility modules
│   ├── yahoo_data_loader.py
│   ├── plot_saver.py
│   └── ...
├── environment.yml             # Conda environment configuration
├── LICENSE
└── README.md
```

---

##  Getting Started

### 1. Install dependencies

```bash
conda env create -f environment.yml
conda activate quant-backtrader
```

### 2. Run a strategy

```bash
python backtests/backtest_sma.py
```

---

## Implemented Strategies

| Strategy | File | Description |
|----------|------|-------------|
| SMA (Simple Moving Average) | `bt_sma_strategy.py` | Fast/slow MA crossover |
| SMA Crossover (with SL/TP) | `bt_sma_crossover.py` | Includes stop-loss and take-profit |
| RSI | `bt_rsi_strategy.py` | Mean-reversion based on RSI levels |
| MACD | `bt_macd_strategy.py` | Trend-following using MACD |
| Bollinger Bands | `bt_bollinger_strategy.py` | Channel breakout strategy |


---

## License

MIT License

---

## Author

Made by Jiawei Wang, a first year mathematical student in UCL.