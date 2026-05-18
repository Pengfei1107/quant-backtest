import yfinance as yf
import numpy as np

# 组合A：三只新能源（高度相关 = 伪分散）
A = ['1211.HK', '300750.SZ', 'TSLA']
# 组合B：跨品类（低相关 = 真分散）
B = ['1211.HK', '601857.SS', 'GLD']

# 循环计算两个组合
for name, syms in [('A', A), ('B', B)]:
    # 下载数据
    df = yf.download(syms, period='3y', auto_adjust=True)['Close'].dropna() # type: ignore
    ret = df.pct_change().dropna()

    # 年化协方差矩阵
    cov = ret.cov() * 252 # type: ignore
    # 等权配置
    w = np.array([1/3, 1/3, 1/3])
    # 组合波动率
    port_vol = np.sqrt(w @ cov @ w) * 100

    print(f"组合 {name} 波动率 = {port_vol:.2f}%")