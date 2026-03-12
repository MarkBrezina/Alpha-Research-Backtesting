
class BacktestEngine:

    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy

    def run(self):

        signals = self.strategy(self.data)

        returns = signals.shift(1) * self.data.pct_change()

        return returns
