import re

def is_valid_hostname(var_0):
    if var_0[-1] == ".":
        # strip exactly one dot from the right, if present
        var_0 = var_0[:-1]
    if len(var_0) > 253:
        return False

    var_1 = var_0.split(".")

    # the TLD must be not all-numeric
    if re.match(r"[0-9]+$", var_1[-1]):
        return False

    var_2 = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(var_2.match(label) for label in var_1)
