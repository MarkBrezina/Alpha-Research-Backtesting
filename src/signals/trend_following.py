
def trend_signal(price, window=50):

    ma = price.rolling(window).mean()

    signal = (price > ma).astype(int)

    return signal
