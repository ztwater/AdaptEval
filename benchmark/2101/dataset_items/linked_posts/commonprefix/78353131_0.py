def common_prefix(strings: list[str]) -> str:
    shortest = min(strings, key=len)
    for i, c in enumerate(shortest):
        if any(x[i] != c for x in strings):
            return shortest[:i]
    return shortest

assert common_prefix(["Abc01", "Abc02", "Abc03"]) == "Abc0"
assert common_prefix(["Abc01", "Abc01"]) == "Abc01"
assert common_prefix(["", "Abc01"]) == ""
assert common_prefix(["Xyz01", "Abc01"]) == ""
