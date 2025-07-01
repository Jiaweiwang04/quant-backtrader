import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import backtrader as bt
import pandas as pd
from strategies.bt_sma_strategy import SmaStrategy
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv('data/sample_data.csv', index_col='Date', parse_dates=True)
bt_data = bt.feeds.PandasData(dataname=data)

# Create a Backtrader engine
cerebro = bt.Cerebro()
cerebro.addstrategy(SmaStrategy)
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
figs[0][0].savefig('images/backtest_sma_result.png')
print("Backtest plot saved to images/result_plot.png")
