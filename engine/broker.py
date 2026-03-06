class Broker:

    def __init__(self, cash: float, commission: float, slippage: float):
        self.cash = cash
        self.position = 0
        self.commission = commission
        self.slippage = slippage

    def buy(self, price: float):

        price = price * (1 + self.slippage)

        cost = price * (1 + self.commission)

        if self.cash >= cost:

            self.position = 1
            self.cash -= cost

            return cost

        return 0

    def sell(self, price: float):

        if self.position == 0:
            return 0

        price = price * (1 - self.slippage)

        revenue = price * (1 - self.commission)

        self.position = 0
        self.cash += revenue

        return revenue