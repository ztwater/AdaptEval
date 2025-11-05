import pandas as pd
import matplotlib.pylab as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

data = pd.read_table("data.dat", sep=",", names=["time", "pressure"])
sub_data = data[data.time > 21.5]

result = lowess(sub_data.pressure, sub_data.time.values)
x_smooth = result[:,0]
y_smooth = result[:,1]

tot_result = lowess(data.pressure, data.time.values, frac=0.1)
x_tot_smooth = tot_result[:,0]
y_tot_smooth = tot_result[:,1]

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(data.time.values, data.pressure, label="raw")
ax.plot(x_tot_smooth, y_tot_smooth, label="lowess 1%", linewidth=3, color="g")
ax.plot(x_smooth, y_smooth, label="lowess", linewidth=3, color="r")
plt.legend()
