import backtrader as bt

class SmaCrossover(bt.Strategy):
    params = dict(pfast = 10, pslow = 30)
    def __init__(self):
        self.sma10 = bt.indicators.MovingAverageSimple(self.data.close, period=self.p.pfast )
        self.sma30 = bt.indicators.MovingAverageSimple(self.data.close, period=self.p.pslow )

    def next(self):
        if self.sma10[0] > self.sma30[0] and self.sma10[-1] < self.sma30[-1]:
            if not self.position:
                self.buy()
        elif self.sma10[0] < self.sma30[0] and self.sma10[-1] < self.sma30[-1]:
            if self.position:
                self.close()