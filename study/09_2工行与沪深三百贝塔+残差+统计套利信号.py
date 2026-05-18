# 文件名：工行沪深三百贝塔残差套利.py
import yfinance as yf
import statsmodels.api as sm
import numpy as np
import pandas as pd

# ===================== 1. 下载数据 & 回归模型 =====================
df = yf.download(['601398.SS','000300.SS'], period='3y', auto_adjust=True)['Close']
ret = df.pct_change().dropna()
y = ret['601398.SS']
x = ret['000300.SS']
model = sm.OLS(y, sm.add_constant(x)).fit()

# ===================== 2. 计算残差 & 累计残差 =====================
y_pred = model.predict(sm.add_constant(x))
residual = y - y_pred
cum_resid = residual.cumsum()
change_30d = cum_resid.iloc[-1] - cum_resid.iloc[-30]

# ===================== 3. 统计套利交易信号（兼容所有版本） =====================
rolling_20 = residual.rolling(20).sum().dropna()

# 分位数分组（无ordered参数，100%不报错）
q5 = pd.qcut(rolling_20, 5, labels=False)  # 输出 0,1,2,3,4

# 自定义信号：0=SELL,1=SELL,2=HOLD,3=BUY,4=BUY
signal = q5.map({0: "SELL", 1: "SELL", 2: "HOLD", 3: "BUY", 4: "BUY"})

# ===================== 输出结果 =====================
print("="*50)
print("【工行 沪深300 贝塔回归】")
print(f"β = {model.params.iloc[1]:.3f}")
print(f"α = {model.params.iloc[0]:+.5f}")
print(f"R² = {model.rsquared:.3f}")
print("="*50)

print("【残差信号】")
print(f"近30天累计残差变化 = {change_30d:+.4%}")
print(f"当前交易信号 = {signal.iloc[-1]}")
print("="*50)