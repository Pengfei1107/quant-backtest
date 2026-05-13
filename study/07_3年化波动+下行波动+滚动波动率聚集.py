# 多资产波动率对比工具箱：年化波动 / 下行波动 / 滚动波动
import yfinance as yf
import numpy as np
import pandas as pd

# 6大标的字典
tickers = {
    '沪深三百': '000300.SS',
    '标普五百': '^GSPC',        # 修复：正确标普代码
    '五粮液': '000858.SZ',
    '中国国债ETF': '511010.SS',
    '比特币': 'BTC-USD',
    '以太坊': 'ETH-USD'
}

# 下载3年收盘价（自动对齐日期）
raw = yf.download(list(tickers.values()), period='3y', auto_adjust=True)['Close'] # type: ignore

# 把列名换成中文（非常关键！）
df = pd.DataFrame({name: raw[ticker] for name, ticker in tickers.items()}).dropna()

# 日收益率
ret = df.pct_change().dropna()

# ===================== 核心指标计算 =====================
ann_vol = ret.std() * np.sqrt(252) * 100    # 年化波动率
down_vol = ret[ret < 0].std() * np.sqrt(252) * 100  # 下行波动率
rolling_21d_vol = ret.rolling(21).std() * np.sqrt(252) * 100  # 21日滚动波动

# ===================== 输出整齐表格 =====================
print("="*50)
print("📊 各大资产风险指标对比（%）")
print("="*50)

vol_table = pd.DataFrame({
    '年化波动(%)': ann_vol.round(1),
    '下行波动(%)': down_vol.round(1)
})

print(vol_table)