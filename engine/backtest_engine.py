import pandas as pd
from engine.broker import Broker
from engine.portfolio import Portfolio

class BacktestEngine:

    def __init__(self, data: pd.DataFrame, strategy):

        self.data = data
        self.strategy = strategy

        self.broker = Broker(
            cash=10000,
            commission=0.001,
            slippage=0.0005
        )

        self.portfolio = Portfolio(10000)

    def run(self):

        for i in range(len(self.data)):

            price = self.data["close"].iloc[i]

            signal = self.strategy.generate_signal(self.data, i)

            if signal == 1:
                self.broker.buy(price)

            elif signal == -1:
                self.broker.sell(price)

            self.portfolio.update(
                self.broker.cash,
                self.broker.position,
                price
            )

        return self.portfolio.equity_curve