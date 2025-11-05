def abbreviate(value, base=1000, precision=2, suffixes=None):
    if suffixes is None:
        suffixes = ['', 'K', 'M', 'B', 'T']

    if value == 0:
        return f'{0}{suffixes[0]}'

    order_max = len(suffixes) - 1
    order = log(abs(value), base)
    order_corr = order - int(order) >= log(base - 0.5/10**precision, base)
    order = min(int(order) + order_corr, order_max)

    factored = round(value/base**order, precision)

    return f'{factored:,g}{suffixes[order]}'
