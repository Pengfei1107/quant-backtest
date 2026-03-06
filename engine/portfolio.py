class Portfolio:

    def __init__(self, initial_cash: float):

        self.initial_cash = initial_cash
        self.equity_curve = []

    def update(self, cash: float, position: int, price: float):

        value = cash + position * price

        self.equity_curve.append(value)