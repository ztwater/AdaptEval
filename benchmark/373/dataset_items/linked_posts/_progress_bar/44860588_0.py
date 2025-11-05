def bar(total, current, length=10, prefix="", filler="#", space=" ", oncomp="", border="[]", suffix=""):
    if len(border) != 2:
        print("parameter 'border' must include exactly 2 symbols!")
        return None

    print(prefix + border[0] + (filler * int(current / total * length) +
                                      (space * (length - int(current / total * length)))) + border[1], suffix, "\r", end="")
    if total == current:
        if oncomp:
            print(prefix + border[0] + space * int(((length - len(oncomp)) / 2)) +
                  oncomp + space * int(((length - len(oncomp)) / 2)) + border[1], suffix)
        if not oncomp:
            print(prefix + border[0] + (filler * int(current / total * length) +
                                        (space * (length - int(current / total * length)))) + border[1], suffix)
