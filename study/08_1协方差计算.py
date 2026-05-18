# 比亚迪 vs 宁德时代 协方差计算
import numpy as np
import pandas as pd
import yfinance as yf

# 下载数据：比亚迪(1211.HK) + 宁德时代(300750.SZ) 近两年收益
df = yf.download(
    ['1211.HK', '300750.SZ'],
    period='2y',
    auto_adjust=True
)['Close'].pct_change().dropna() # type: ignore

# 拆分两列收益
byd = df.iloc[:, 0] # type: ignore
catl = df.iloc[:, 1] # type: ignore

# ===================== 协方差手动计算 =====================
# 1. 算出每天的偏离量（相对于自身均值）
dev_byd = byd - byd.mean()
dev_catl = catl - catl.mean()

# 2. 协方差 = 偏离量乘积的平均值（样本用 N-1 修正）
cov = (dev_byd * dev_catl).sum() / (len(byd) - 1)

# 输出结果
print(f'比亚迪 ↔ 宁德时代 协方差 = {cov:.6f}')
print('→ 正数 = 同涨同跌；负数 = 反向走；接近0 = 没关系')