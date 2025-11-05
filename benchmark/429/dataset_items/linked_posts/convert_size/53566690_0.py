def human_size(num: int) -> str:
    base = 1
    for unit in ['B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
        n = num / base
        if n < 9.95 and unit != 'B':
            # Less than 10 then keep 1 decimal place
            value = "{:.1f}{}".format(n, unit)
            return value
        if round(n) < 1000:
            # Less than 4 digits so use this
            value = "{}{}".format(round(n), unit)
            return value
        base *= 1024
    value = "{}{}".format(round(n), unit)
    return value
