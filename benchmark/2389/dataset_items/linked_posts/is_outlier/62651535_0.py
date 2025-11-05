mean = np.mean(imgs, axis=0)
std = np.std(imgs, axis=0)
mask = np.greater(0.5 * std + 1, np.abs(imgs - mean))
masked = np.multiply(imgs, mask)
