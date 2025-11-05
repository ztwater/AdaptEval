def longest_increasing_subsequence_indices(seq):
    from bisect import bisect_right

    if len(seq) == 0:
        return seq

    # m[j] in iteration i is the last index of the increasing subsequence of seq[:i]
    # that ends with the lowest possible value while having length j
    m = [None] * len(seq)
    predecessor = [None] * len(seq)
    best_len = 0

    for i, item in enumerate(seq):
        j = bisect_right([seq[k] for k in m[:best_len]], item)
        m[j] = i
        predecessor[i] = m[j-1] if j > 0 else None
        best_len = max(best_len, j+1)

    result = []
    i = m[best_len-1]
    while i is not None:
        result.append(i)
        i = predecessor[i]
    result.reverse()
    return result

def longest_increasing_subsequence(seq):
    return [seq[i] for i in longest_increasing_subsequence_indices(seq)]
