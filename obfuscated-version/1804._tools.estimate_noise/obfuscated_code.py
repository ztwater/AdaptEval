def estimate_noise(var_0):

  H, W = var_0.shape

  var_1 = [[1, -2, 1],
       [-2, 4, -2],
       [1, -2, 1]]

  var_2 = np.sum(np.sum(np.absolute(convolve2d(var_0, var_1))))
  var_2 = var_2 * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))

  return var_2
