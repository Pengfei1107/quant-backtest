import pandas as pd

class BacktestEngine:
    def __init__(self, data_path, initial_cash):
        self.data = pd.read_csv(data_path)
        self.cash = initial_cash
        self.position = 0
        self.trades = []

    def run(self, strategy):
        for i in range(len(self.data)):
            signal = strategy.generate_signal(self.data, i)
            self._handle_signal(signal, self.data.iloc[i])

    def _handle_signal(self, signal, row):
        if signal == "BUY" and self.cash > 0:
            self.position = self.cash / row["close"]
            self.cash = 0
            self.trades.append(("BUY", row["date"], row["close"]))

        elif signal == "SELL" and self.position > 0:
            self.cash = self.position * row["close"]
            self.position = 0
            self.trades.append(("SELL", row["date"], row["close"]))

    def report(self):
        print("Trades:")
        for t in self.trades:
            print(t)
        print("Final cash:", self.cash)