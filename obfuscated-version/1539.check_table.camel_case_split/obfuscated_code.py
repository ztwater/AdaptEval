def camel_case_split(var_0):
    var_1 = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', var_0)
    return [m.group(0) for m in var_1]
