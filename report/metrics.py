import numpy as np

def max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0
    for v in equity_curve:
        peak = max(peak, v)
        max_dd = min(max_dd, (v - peak) / peak)
    return max_dd

def sharpe(returns, risk_free=0):
    return np.mean(returns - risk_free) / np.std(returns)