plt.rcParams['image.cmap'] = 'Paired'

plt.figure(figsize=(6, 6))
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.quiver(x, y, u, v, np.arctan2(v, u), angles='xy', scale_units='xy', scale=1, pivot='mid')
