import yfinance as yf
import pandas as pd

# 核心资产字典（修复所有符号、引号、拼写错误）
tickers = {
    '沪深三百': '000300.SS',
    '恒生指数': '^HSI',
    '标普五百': '^GSPC',
    '黄金': 'GC=F',
    '比特币': 'BTC-USD'
}

# 下载5年收盘价数据
data = {name: yf.download(ticker, period='5y')['Close'] for name, ticker in tickers.items()} # type: ignore

# 合并数据 + 剔除缺失值
df = pd.concat(data, axis=1).dropna()

# 净值归一（起点=1）
norm = df / df.iloc[0]

# 计算：5年总收益率(%) + 年化波动率(%)
ret_5y = (norm.iloc[-1] - 1) * 100  # 总收益
vol_ann = df.pct_change().std() * (252 ** 0.5) * 100  # 年化波动

# 输出干净表格
result = pd.DataFrame({
    '5年总收益率(%)': ret_5y.round(2),
    '年化波动率(%)': vol_ann.round(2)
})
print("===== 全球核心资产5年表现 =====")
print(result)