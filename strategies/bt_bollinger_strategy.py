import backtrader as bt

class BollingerStrategy(bt.Strategy):
    params = dict(
        period = 20,
        devfactor = 2.0
    )

    def __init__(self):
        self.bb = bt.indicators.BollingerBands(
            self.data.close,
            period = self.p.period,
            devfactor = self.p.devfactor                                   
        )

    def next(self):
        if not self.position:
            if self.data.close[0] < self.bb.lines.bot[0]:
                self.buy()

        else:
            if self.data.close[0] > self.bb.lines.mid[0]:
                self.sell()
