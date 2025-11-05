>>> x, y = np.meshgrid(x, y)
>>> np.concatenate([x.flatten().reshape(-1,1), y.flatten().reshape(-1,1)], axis=1)
