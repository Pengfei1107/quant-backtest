# 收益率工具箱：5 种算法一次跑五个标的
import yfinance as yf
import numpy as np

# 5 个标的：A股、港股、美股、黄金、比特币
tickers = ['600036.SS', '3690.HK', 'MSFT', 'GLD', 'BTC-USD']

# 下载 3 年收盘价数据（自动复权 + 去缺失值）
df = yf.download(tickers, period='3y', auto_adjust=True)['Close'].dropna() # type: ignore


# ===================== 1. 简单收益率 =====================
simple_ret = df.pct_change().dropna()

# ===================== 2. 对数收益率 =====================
log_ret = np.log(df / df.shift(1)).dropna() # type: ignore

# ===================== 3. 累计简单收益率 =====================
cum_simple = (1 + simple_ret).cumprod() - 1

# ===================== 4. 年化收益 & 年化波动 =====================
ann_ret = (1 + simple_ret.mean()) ** 252 - 1  # 年化收益
ann_vol = simple_ret.std() * np.sqrt(252)     # 年化波动

# ===================== 5. 夏普比率 =====================
sharpe = ann_ret / ann_vol  # 夏普比率

# ===================== 输出结果 =====================
print("===== 年化收益率(%) =====")
print((ann_ret * 100).round(2)) # type: ignore
print("\n===== 年化波动率(%) =====")
print((ann_vol * 100).round(2))
print("\n===== 夏普比率 =====")
print(sharpe.round(2))