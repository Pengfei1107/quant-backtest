import statsmodels.tsa.stattools as ts
import pandas as pd
import numpy as np

# ======================
# 1. 统计套利：配对协整检验
# ======================
# 模拟数据（你可以替换成真实股票数据）
stock_a = np.random.normal(0, 1, 100)  # 股票A价格序列
stock_b = np.random.normal(0, 1, 100)  # 股票B价格序列
hedge_ratio = 1.0                      # 对冲比例

spread = stock_a - hedge_ratio * stock_b
p_value, *_ = ts.adfuller(spread)

print('p =', p_value)
print('-可做配对' if p_value < 0.05 else '-不显著')

# ======================
# 2. 高频做市：订单簿不平衡（OFI）
# ======================
bid_size = 1000  # 买盘量
ask_size = 800   # 卖盘量

ofi = (bid_size - ask_size) / (bid_size + ask_size)

print('OFI =', ofi)
print('-短期看涨' if ofi > 0.1 else '-观望')

# ======================
# 3. 因子投资：四因子等权打分选股
# ======================
# 模拟因子数据
factors = pd.DataFrame({
    'value': np.random.rand(50),
    'momentum': np.random.rand(50),
    'quality': np.random.rand(50),
    'low vol': np.random.rand(50)
})

# 四因子等权打分
score = factors[['value', 'momentum', 'quality', 'low vol']].mean(axis=1)
top_30 = score.nlargest(30).index.tolist()

print('头部30只股票均值：', score[top_30].mean())
print('尾部股票均值：', score[~score.index.isin(top_30)].mean())