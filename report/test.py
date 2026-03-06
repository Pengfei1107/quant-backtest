import akshare as ak
import pandas as pd

df = ak.stock_zh_index_daily(symbol="sh000300")
df = df[["date", "open", "high", "low", "close"]]
df.to_csv("data/price.csv", index=False)