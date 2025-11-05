import finplot as fplt
import yfinance

var_0 = 'AAPL'
var_1 = yfinance.download(var_0)

var_2 = fplt.create_plot(var_0)

fplt.candlestick_ochl(var_1[['Open', 'Close', 'High', 'Low']], var_2=var_2)
fplt.plot(var_1['Close'].rolling(200).mean(), var_2=var_2, legend='SMA 200')
fplt.plot(var_1['Close'].rolling(50).mean(), var_2=var_2, legend='SMA 50')
fplt.plot(var_1['Close'].rolling(20).mean(), var_2=var_2, legend='SMA 20')

fplt.volume_ocv(var_1[['Open', 'Close', 'Volume']], var_2=var_2.overlay())

fplt.show()
