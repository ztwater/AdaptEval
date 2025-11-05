def humanized_size(num, suffix='B', si=False):
    if si:
        units = ['','K','M','G','T','P','E','Z']
        last_unit = 'Y'
        div = 1000.0
    else:
        units = ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']
        last_unit = 'Yi'
        div = 1024.0
    for unit in units:
        if abs(num) < div:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= div
    return "%.1f%s%s" % (num, last_unit, suffix)
