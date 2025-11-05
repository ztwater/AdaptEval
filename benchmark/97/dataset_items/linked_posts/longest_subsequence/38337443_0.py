from bisect import bisect_left, bisect_right
from functools import cmp_to_key

def longest_subsequence(seq, mode='strictly', order='increasing',
                        key=None, index=False):

  bisect = bisect_left if mode.startswith('strict') else bisect_right

  # compute keys for comparison just once
  rank = seq if key is None else map(key, seq)
  if order == 'decreasing':
    rank = map(cmp_to_key(lambda x,y: 1 if x<y else 0 if x==y else -1), rank)
  rank = list(rank)

  if not rank: return []

  lastoflength = [0] # end position of subsequence with given length
  predecessor = [None] # penultimate element of l.i.s. ending at given position

  for i in range(1, len(seq)):
    # seq[i] can extend a subsequence that ends with a lesser (or equal) element
    j = bisect([rank[k] for k in lastoflength], rank[i])
    # update existing subsequence of length j or extend the longest
    try: lastoflength[j] = i
    except: lastoflength.append(i)
    # remember element before seq[i] in the subsequence
    predecessor.append(lastoflength[j-1] if j > 0 else None)

  # trace indices [p^n(i), ..., p(p(i)), p(i), i], where n=len(lastoflength)-1
  def trace(i):
    if i is not None:
      yield from trace(predecessor[i])
      yield i
  indices = trace(lastoflength[-1])

  return list(indices) if index else [seq[i] for i in indices]
