import pandas as pd
from strategy.base_strategy import BaseStrategy

class MovingAverageStrategy(BaseStrategy):

    def __init__(self, short_window: int = 5, long_window: int = 20):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self, data: pd.DataFrame, index: int) -> int:

        if index < self.long_window:
            return 0

        short_ma = data["close"].iloc[index-self.short_window:index].mean()
        long_ma = data["close"].iloc[index-self.long_window:index].mean()

        if short_ma > long_ma:
            return 1
        elif short_ma < long_ma:
            return -1
        else:
            return 0