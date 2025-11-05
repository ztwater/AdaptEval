def unix_time() -> int:
    return int(time.time())


def pretty_time(t: int, absolute=False) -> str:
    if not type(t) is int:
        return "N/A"
    if t == 0:
        return "Never"

    now = unix_time()
    if t == now:
        return "Now"

    periods = ["second", "minute", "hour", "day", "week", "month", "year", "decade"]
    lengths = [60, 60, 24, 7, 4.35, 12, 10]

    diff = now - t

    if absolute:
        suffix = ""
    else:
        if diff >= 0:
            suffix = "ago"
        else:
            diff *= -1
            suffix = "remaining"

    i = 0
    while diff >= lengths[i] and i < len(lengths) - 1:
        diff /= lengths[i]
        i += 1

    diff = round(diff)
    if diff > 1:
        periods[i] += "s"

    return "{0} {1} {2}".format(diff, periods[i], suffix)
