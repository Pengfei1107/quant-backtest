import numpy as np

def annual_return(equity):

    total_return = equity[-1] / equity[0] - 1

    years = len(equity) / 252

    return (1 + total_return) ** (1/years) - 1


def max_drawdown(equity):

    peak = equity[0]
    max_dd = 0

    for v in equity:

        if v > peak:
            peak = v

        dd = (peak - v) / peak

        if dd > max_dd:
            max_dd = dd

    return max_dd


def sharpe_ratio(equity):

    returns = np.diff(equity) / equity[:-1]

    return np.mean(returns) / np.std(returns) * np.sqrt(252)