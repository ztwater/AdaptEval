import numpy as np


def common_prefix(strings: list[str]) -> str:
    # common prefix cannot be larger than the smallest str
    min_length = min(len(string) for string in strings)
    strings = [string[:min_length] for string in strings]

    array = np.array([list(x) for x in strings])  # covert to numpy matrix for column-wise operations
    for i in range(min_length):
        # for every column check if all char values are the same (same as first)
        if not all(array[:, i] == array[0][i]):
            # if not return the substring before the first char difference
            return strings[0][:i]

    # the common prefix is the full (shortest) str
    return strings[0]


assert common_prefix(["str1", "str2", "str3"]) == "str"
assert common_prefix(["s", "st", "str"]) == "s"
assert common_prefix(["1str", "str", "str"]) == ""

