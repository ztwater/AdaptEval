def weight_array(ar, weights):
     zipped = zip(ar, weights)
     weighted = []
     for a, w in zipped:
         for j in range(w):
             weighted.append(a)
     return weighted


np.percentile(weight_array(ar, weights), 25)
