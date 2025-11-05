from bisect import bisect_left, bisect_right
from functools import cmp_to_key

def longest_subsequence(var_0, var_1='strictly', var_2='increasing',
                        var_3=None, var_4=False):

  var_5 = bisect_left if var_1.startswith('strict') else bisect_right

  # compute keys for comparison just once
  var_6 = var_0 if var_3 is None else map(var_3, var_0)
  if var_2 == 'decreasing':
    var_6 = map(cmp_to_key(lambda x,y: 1 if x<y else 0 if x==y else -1), var_6)
  var_6 = list(var_6)

  if not var_6: return []

  var_7 = [0] # end position of subsequence with given length
  var_8 = [None] # penultimate element of l.i.s. ending at given position

  for i in range(1, len(var_0)):
    # seq[i] can extend a subsequence that ends with a lesser (or equal) element
    var_9 = var_5([var_6[k] for k in var_7], var_6[i])
    # update existing subsequence of length j or extend the longest
    try: var_7[var_9] = i
    except: var_7.append(i)
    # remember element before seq[i] in the subsequence
    var_8.append(var_7[var_9-1] if var_9 > 0 else None)

  # trace indices [p^n(i), ..., p(p(i)), p(i), i], where n=len(lastoflength)-1
  def trace(var_10):
    if var_10 is not None:
      yield from trace(var_8[var_10])
      yield var_10
  var_11 = trace(var_7[-1])

  return list(var_11) if var_4 else [var_0[var_10] for var_10 in var_11]
