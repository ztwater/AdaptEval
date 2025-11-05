import finplot as fplt

def plot_candle_patter(df):
    #https://stackoverflow.com/questions/9673988/intraday-candlestick-charts-using-matplotlib
    ax = fplt.create_plot("symbol")


    fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']], ax=ax)
    fplt.plot(df['Close'].rolling(200).mean(), ax=ax, legend='SMA 200')
    fplt.plot(df['Close'].rolling(50).mean(), ax=ax, legend='SMA 50')
    fplt.plot(df['Close'].rolling(20).mean(), ax=ax, legend='SMA 20')

    #df.set_index('Date', inplace=True)
    fplt.volume_ocv(df[['Open', 'Close', 'Volume']] , ax=ax.overlay() )

    fplt.show()