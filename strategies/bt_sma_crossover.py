import backtrader as bt

class SmaCrossover(bt.Strategy):
    def __init__(self):
        self.sma10 = bt.indicators.MovingAverageSimple(self.data.close, period=10 )
        self.sma30 = bt.indicators.MovingAverageSimple(self.data.close, period=30 )

    def next(self):
        if self.sma10[0] > self.sma30[0] and self.sma10[-1] < self.sma30[-1]:
            if not self.position:
                self.buy()
        elif self.sma10[0] < self.sma30[0] and self.sma10[-1] < self.sma30[-1]:
            if self.position:
                self.close()