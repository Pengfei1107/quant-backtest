# 沪深300近30天日收益 —— 手动计算标准差（五步拆解）
import numpy as np
import pandas as pd
import yfinance as yf

# 下载沪深300ETF(510300)近30天数据
ret = yf.download(
    '510300.SS',
    period='30d',
    auto_adjust=True
)['Close'].squeeze().pct_change().dropna() # type: ignore

# ===================== 五步手动计算标准差 =====================
mean = ret.mean()                # ① 平均收益
dev = ret - mean                 # ② 每日偏离量
sq_dev = dev ** 2                # ③ 偏离平方（消除正负）
var = sq_dev.sum() / (len(ret)-1) # ④ 方差（样本方差 N-1 修正）
std = np.sqrt(var)               # ⑤ 标准差 = 日波动率

# ===================== 输出结果 =====================
print(f'日均收益 {mean:+.4%} | 日波动率 {std:.4%}')
print('日波动率就是沪深300的“刺激度”')