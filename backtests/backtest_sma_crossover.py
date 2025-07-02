import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
from strategies.bt_sma_crossover import SmaCrossover
from utils.akshare_data_loader import download_cn_data

# load CSV data
download_cn_data("600519","20220101","20230101","data/maotai_sample.csv")
data = pd.read_csv("data/maotai_sample.csv", index_col='Date', parse_dates=True)
bt_data = bt.feeds.PandasData(dataname=data)

# create a backtrader engine
cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCrossover)
cerebro.adddata(bt_data)
cerebro.broker.set_cash(10000)

# Print initial capital
print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

# Run backtest
cerebro.run()

# Print final capital
print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

# Plot & Save
figs = cerebro.plot(style='candlestick')
figs[0][0].savefig('images/backtest_sma_crossover_result.png')
print("Backtest plot saved to images/backtest_sma_crossover_result.png")

