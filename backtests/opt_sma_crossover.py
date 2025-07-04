import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import backtrader as bt
import pandas as pd
from strategies.bt_sma_crossover import SmaCrossover
from utils.akshare_data_loader import download_cn_data

# load CSV data
download_cn_data("600519","20220101","20230101","data/maotai_sample.csv")
data = pd.read_csv("data/maotai_sample.csv", index_col='Date', parse_dates=True)
bt_data = bt.feeds.PandasData(dataname=data)

# create a backtrader engine
cerebro = bt.Cerebro(optreturn=True)
cerebro.adddata(bt_data)
cerebro.broker.set_cash(10000)

# add optimize
cerebro.optstrategy(SmaCrossover, pfast = range(5,21,5), pslow = range(30,61,5))

# add performance analysis
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe")
cerebro.addanalyzer(bt.analyzers.DrawDown, _name="drawdown")
cerebro.addanalyzer(bt.analyzers.Returns, _name="returns")

# Run backtest
results = cerebro.run()

# get results
records = []

for start in results:
    s = start[0]
    sharpe = s.analyzers.sharpe.get_analysis().get("sharperatio",None)
    max_drawdown = s.analyzers.drawdown.get_analysis().get("max",{}).get("drawdown",None)
    ret = s.analyzers.returns.get_analysis().get("rtot",None)
    records.append({
        "pfast": s.params.pfast,
        "pslow": s.params.pslow,
        "sharpe": sharpe,
        "return": ret,
        "max_drawdown": max_drawdown
    }
    )

# save results
df = pd.DataFrame(records)
df.to_csv("docs/result_sma_opt.csv", index=False)

print("optimization results have saved in docs/result_sma_opt.csv")
