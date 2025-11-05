In [328]: from statsmodels.nonparametric.smoothers_lowess import lowess

In [329]: filtered = lowess(pressure, time, is_sorted=True, frac=0.025, it=0)

In [330]: plot(time, pressure, 'r')
Out[330]: [<matplotlib.lines.Line2D at 0x1178d0668>]

In [331]: plot(filtered[:,0], filtered[:,1], 'b')
Out[331]: [<matplotlib.lines.Line2D at 0x1173d4550>]
