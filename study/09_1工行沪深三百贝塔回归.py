# 文件名：工行沪深三百贝塔回归.py
# 工行与沪深三百近三年日收益贝塔阿尔法测算
import yfinance as yf
import statsmodels.api as sm

# 下载行情数据
df = yf.download(['601398.SS','000300.SS'], period='3y', auto_adjust=True)['Close'] # type: ignore

# 计算日收益率
ret = df.pct_change().dropna()

# 定义变量
y = ret['601398.SS']
x = ret['000300.SS']

# 最小二乘回归
model = sm.OLS(y, sm.add_constant(x)).fit()

# 输出结果（已修复 FutureWarning 警告）
print(f'β={model.params.iloc[1]:.3f}')
print(f'α={model.params.iloc[0]:+.5f}')
print(f'R²={model.rsquared:.3f}')
print(f'α统计量={model.tvalues.iloc[0]:.2f}')