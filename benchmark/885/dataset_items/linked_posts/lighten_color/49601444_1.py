import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-1, 1, 100)
plt.plot(xs, 0 * xs, color='b', lw=3)
plt.plot(xs, xs**2, color=lighten_color('b', 0.4), lw=3)
plt.plot(xs, -xs**2, color=lighten_color('b', 1.6), lw=3)
