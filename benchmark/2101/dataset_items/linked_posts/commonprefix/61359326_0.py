from collections import Counter

def get_longest_common_prefix(values, min_length):
    substrings = [value[0: i-1] for value in values for i in range(min_length, len(value))]
    counter = Counter(substrings)
    # remove count of 1
    counter -= Counter(set(substrings))
    return max(counter, key=len)
