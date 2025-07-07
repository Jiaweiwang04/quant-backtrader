import backtrader as bt

class RsiStrategy(bt.Strategy):
    params = dict(
        rsi_period = 14,
        rsi_oversold = 30,
        rsi_overbought = 70
    )

    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close,period = self.p.rsi_period)

    def next(self):
        if not self.position:
            if self.rsi < self.p.rsi_oversold:
                self.buy()
        
        elif self.rsi > self.p.rsi_overbought:
            self.close()
