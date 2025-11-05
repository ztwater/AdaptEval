def maybeMakeNumber(s):
    """Returns a string 's' into a integer if possible, a float if needed or
    returns it as is."""

    # handle None, "", 0
    if not s:
        return s
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        return s

data = ["unkind", "data", "42", 98, "47.11", "of mixed", "types"]

converted = list(map(maybeMakeNumber, data))
print(converted)
