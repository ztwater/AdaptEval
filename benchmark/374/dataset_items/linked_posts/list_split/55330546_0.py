def chunk_ports(port_start, port_end, portions):
    if port_end < port_start:
        return None

    total = port_end - port_start + 1

    fractions = int(math.floor(float(total) / portions))

    results = []

    # No enough to chuck.
    if fractions < 1:
        return None

    # Reverse, so any additional items would be in the first range.
    _e = port_end
    for i in range(portions, 0, -1):
        print "i", i

        if i == 1:
            _s = port_start
        else:
            _s = _e - fractions + 1

        results.append((_s, _e))

        _e = _s - 1

    results.reverse()

    return results
