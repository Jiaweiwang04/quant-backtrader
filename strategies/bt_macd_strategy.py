import backtrader as bt

class MACDStrategy(bt.Strategy):
    params = dict(
        slow_period = 26,
        fast_period = 12,
        signal_period = 9
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1 = self.p.fast_period,
            period_me2 = self.p.slow_period,
            period_signal = self.p.signal_period
        )
        self.cross_over = bt.ind.CrossOver(self.macd.macd, self.macd.signal)

    def next(self):
        if not self.position:
            if self.cross_over > 0:
                self.buy()
        
        else:
            if self.cross_over < 0:
                self.close()                    