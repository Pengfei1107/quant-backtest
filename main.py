import pandas as pd
import matplotlib.pyplot as plt

from strategy.ma_strategy import MovingAverageStrategy
from engine.backtest_engine import BacktestEngine

data = pd.read_csv("data/price.csv")

strategy = MovingAverageStrategy()

engine = BacktestEngine(data, strategy)

equity = engine.run()

plt.plot(equity)
plt.title("Equity Curve")
plt.show()


from report.performance import *

print("平均收益率:", annual_return(equity))
print("最大回撤:", max_drawdown(equity))
print("夏普比率:",  sharpe_ratio(equity))