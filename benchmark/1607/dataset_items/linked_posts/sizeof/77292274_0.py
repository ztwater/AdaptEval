def humanSize(value, decimals=2, scale=1024, units=("B", "kiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB", "RiB", "QiB")):
    for unit in units:
        if value < scale:
            break
        value /= scale
    if int(value) == value:
        # do not return decimals, if the value is already round
        return int(value), unit
    return round(value * 10**decimals) / 10**decimals, unit
