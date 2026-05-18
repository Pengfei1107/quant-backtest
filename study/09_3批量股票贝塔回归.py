# 文件名：批量股票贝塔回归.py
import yfinance as yf
import statsmodels.api as sm

# 股票 : 对标基准
stocks = {
    "601398.SS": "000300.SS",   # 工行 vs 沪深300
    "601012.SS": "000300.SS",   # 隆基 vs 沪深300
    "NVDA": "^GSPC"             # 英伟达 vs 标普500
}

# 批量计算贝塔、阿尔法、年化超额、R²
for stock, bench in stocks.items():
    df = yf.download([stock, bench], period="3y", auto_adjust=True)["Close"].dropna()
    ret = df.pct_change().dropna()
    
    X = sm.add_constant(ret[bench])
    model = sm.OLS(ret[stock], X).fit()
    
    alpha = model.params.iloc[0]
    beta = model.params.iloc[1]
    r2 = model.rsquared
    
    # 输出：贝塔、年化阿尔法、R²
    print("="*50)
    print(f"股票：{stock} | 基准：{bench}")
    print(f"β  = {beta:.2f}")
    print(f"年化α = {alpha*252*100:.1f}%")
    print(f"R² = {r2:.2f}")

print("="*50)