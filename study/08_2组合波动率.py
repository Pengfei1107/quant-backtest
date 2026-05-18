import numpy as np
import pandas as pd
import yfinance as yf

# ===================== 下载3只资产数据 =====================
# 比亚迪、宁德时代、茅台
tickers = ['1211.HK', '300750.SZ', '600519.SS']
df = yf.download(tickers, period='2y', auto_adjust=True)['Close'].pct_change().dropna() # type: ignore
ret = df

# ===================== 核心计算 =====================
Sigma = ret.cov() * 252    # type: ignore # 年化协方差矩阵（N×N）
w = np.array([1/3, 1/3, 1/3])  # 等权配置

# 组合方差 = w · Σ · w
var_p = w @ Sigma @ w
vol_p = np.sqrt(var_p) * 100  # 组合年化波动率

# 错误算法：直接简单平均（没考虑分散投资）
naive = ret.std().mean() * np.sqrt(252) * 100 # type: ignore

# ===================== 输出结果 =====================
print(f'✅ 组合年化波动（矩阵法）= {vol_p:.2f}%')
print(f'❌ 错误平均法（无分散）= {naive:.2f}%')
print(f'📉 分散投资降低风险 = {naive - vol_p:.2f} 个百分点')