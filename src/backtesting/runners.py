
def run_backtest(strategy, data):

    engine = BacktestEngine(data, strategy)

    results = engine.run()

    return results
