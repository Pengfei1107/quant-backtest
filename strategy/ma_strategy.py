import pandas as pd

from strategy.base import BaseStrategy

class MovingAverageStrategy(BaseStrategy):

    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self, data, index):
        if index < self.long_window:
            return None

        short_ma = data["close"].iloc[index-self.short_window:index].mean()
        long_ma = data["close"].iloc[index-self.long_window:index].mean()

        if short_ma > long_ma:
            return "BUY"
        elif short_ma < long_ma:
            return "SELL"
        else:
            return None
