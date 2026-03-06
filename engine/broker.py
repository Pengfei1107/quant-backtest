class Broker:
    def __init__(self, commission=0.001, slippage=0.0005):
        self.commission = commission
        self.slippage = slippage

    def execute(self, price, amount):
        exec_price = price * (1 + self.slippage)
        cost = exec_price * amount
        fee = cost * self.commission
        return exec_price, fee