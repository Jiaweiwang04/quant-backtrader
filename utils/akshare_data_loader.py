import akshare as ak
import os
import pandas as pd

def download_cn_data(symbol: str, start: str, end: str, filename: str):
    """
    下载A股日线数据，保存为CSV文件。

    symbol: 股票代码，如 '600519'
    start: 开始日期，格式 '20220101'
    end: 结束日期，格式 '20230101'
    filename: 保存路径，如 'data/maotai.csv'
    """
    df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date=start,
        end_date=end,
        adjust="qfq"  # 前复权
    )
    df.rename(columns={"日期": "Date", "开盘": "Open", "最高": "High", "最低": "Low",
                       "收盘": "Close", "成交量": "Volume"}, inplace=True)
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
    df.to_csv(filename, index=False)
    print(f"save A股数据 to {filename}")