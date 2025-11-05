def sizeof_fmt(var_0, var_1="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(var_0) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        var_0 /= 1024.0
    return f"{num:.1f}Yi{suffix}"
