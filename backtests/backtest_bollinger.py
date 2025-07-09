import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
from strategies.bt_bollinger_strategy import BollingerStrategy
from utils.akshare_data_loader import download_cn_data
from utils.plot_saver import save_plot
from utils.report_writer import save_analysis_report

# load CSV data
download_cn_data("600519","20220101","20230101","data/maotai_sample.csv")
data = pd.read_csv("data/maotai_sample.csv", index_col='Date', parse_dates=True)
bt_data = bt.feeds.PandasData(dataname=data)

# create a backtrader engine
cerebro = bt.Cerebro()
cerebro.addstrategy(BollingerStrategy)
cerebro.adddata(bt_data)
cerebro.broker.set_cash(10000)

# add performance analysis
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe")
cerebro.addanalyzer(bt.analyzers.DrawDown, _name="drawdown")

# Run backtest
results = cerebro.run()
strategy = results[0]
final_value = cerebro.broker.getvalue()

# save performance report to docs
save_analysis_report(
    strategy,
    filename="bollinger_report.md",
    initial_cash=10000,
    final_value=final_value
) 

# Plot & Save
figs = cerebro.plot(style="candlestick")
save_plot(figs[0][0], filename="backtest_bollinger_result.png")

