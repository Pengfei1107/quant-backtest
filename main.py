from engine.backtest import BacktestEngine
from strategy.ma_strategy import MovingAverageStrategy

def main():
    engine = BacktestEngine(
        data_path="data/price.csv",
        initial_cash=100000
    )

    strategy = MovingAverageStrategy(
        short_window=5,
        long_window=20
    )

    engine.run(strategy)
    engine.report()

if __name__ == "__main__":
    main()
