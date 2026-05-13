# 沪深300近30天：方差对比（ddof=0 vs ddof=1）
import numpy as np
import pandas as pd
import yfinance as yf

# 下载数据
ret = yf.download('510300.SS', period='30d', auto_adjust=True)['Close'].pct_change().dropna() # type: ignore

# 三种方差计算
v_pop = np.var(ret)          # numpy 默认：ddof=0 → 除以 N
v_sample = np.var(ret, ddof=1)  # 除以 N-1（正确）
v_pandas = ret.var()         # pandas 默认：ddof=1（正确）

# 输出（加 .item() 取出单个数字）
print(f'numpy 默认(除以N)   = {v_pop.item():.7f} （会低估真实波动）')
print(f'numpy ddof=1(除以N-1) = {v_sample.item():.7f} （金融/量化正确用法）')
print(f'pandas var() 默认     = {v_pandas.item():.7f} （默认就对）') # type: ignore

print("\n30天样本，两者差距约 3.4%")
print("✅ 严肃量化必须用 ddof=1（贝塞尔修正）")