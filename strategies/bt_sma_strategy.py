import backtrader as bt

class SmaStrategy(bt.Strategy):
    """
    A simple moving average (SMA) crossover strategy.
    Buy when the close price is above the 15-period SMA.
    Sell (close position) when the close price drops below the SMA.
    """

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=15)

    def next(self):
        if self.data.close[0] > self.sma[0]:
            if not self.position:
                self.buy()
        elif self.data.close[0] < self.sma[0]:
            if self.position:
                self.close()
