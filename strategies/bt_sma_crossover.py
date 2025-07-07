import backtrader as bt

class SmaCrossover(bt.Strategy):
    params = dict(pfast = 10, pslow = 30)
    def __init__(self):
        self.sma10 = bt.indicators.MovingAverageSimple(self.data.close, period=self.p.pfast )
        self.sma30 = bt.indicators.MovingAverageSimple(self.data.close, period=self.p.pslow )
        self.cross = bt.ind.CrossOver(self.sma10, self.sma30)
        self.entry_price = None

    def next(self):
        if not self.position:
            if self.cross > 0:
                self.buy()
                self.entry_price = self.data.close[0]
        else:
            change = (self.data.close[0] - self.entry_price) / self.entry_price
            if change <= -0.1 or change >= 0.5:
                self.close()
            elif self.cross < 0:
                self.close()