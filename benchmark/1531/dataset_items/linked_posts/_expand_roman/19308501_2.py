def translate2(string):
    values = {"i":1, "v":5, "x":10, "l":50, "c":100, "m":1000}
    if not string:
        return 0
    return values[string[0]] + translate2(string[1:])
