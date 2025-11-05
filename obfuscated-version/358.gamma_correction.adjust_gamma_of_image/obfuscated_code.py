def adjust_gamma(var_0, var_1=1.0):
   var_2 = 1.0 / var_1
   var_3 = np.array([
      ((i / 255.0) ** var_2) * 255
      for i in np.arange(0, 256)])
   return cv2.LUT(var_0.astype(np.uint8), var_3.astype(np.uint8))
