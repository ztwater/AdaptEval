LEN = 50 #Lookback and Lookforward
OHLC['PivotHigh'] = OHLC['high'] == OHLC['high'].rolling(2 * LEN + 1, center=True).max()
OHLC['PivotLow'] = OHLC['low'] == OHLC['low'].rolling(2 * LEN + 1, center=True).min()
