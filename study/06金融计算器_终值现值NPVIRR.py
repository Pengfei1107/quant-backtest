import numpy as np
from numpy_financial import irr

# 1. 先定义输入数据（必须加，否则代码跑不了）
principal = 10000    # 本金
rate = 0.05          # 年利率 5%
years = 10           # 投资年数
future_cash = 20000  # 未来现金流
discount = 0.05      # 折现率
cash_flows = [-10000, 1000, 1500, 2000, 2500, 8000]  # 现金流：初期投入+未来回收

# 2. 复利终值
fv = principal * (1 + rate) ** years

# 3. 贴现现值
pv = future_cash / ((1 + discount) ** years)

# 4. 净现值 NPV
npv = sum(cf / ((1 + discount) ** t) for t, cf in enumerate(cash_flows))

# 5. 内部收益率 IRR
rate_irr = irr(cash_flows)

# 6. 输出结果
print('终值：', round(fv, 2))
print('现值：', round(pv, 2))
print('NPV：', round(npv, 2))
print('IRR：', round(rate_irr, 4))