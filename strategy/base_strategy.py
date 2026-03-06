from abc import ABC, abstractmethod
import pandas as pd

class BaseStrategy(ABC):

    @abstractmethod
    def generate_signal(self, data: pd.DataFrame, index: int) -> int:
        """
        生成交易信号

        return:
        1 -> buy
        -1 -> sell
        0 -> hold
        """
        pass