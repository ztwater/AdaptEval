def median(items):
    if len(items) % 2:
        return select_nth(len(items)//2, items)

    else:
        left  = select_nth((len(items)-1) // 2, items)
        right = select_nth((len(items)+1) // 2, items)

        return (left + right) / 2
