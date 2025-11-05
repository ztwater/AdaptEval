def translate(string):
    values = {"i":1, "v":5, "x":10, "l":50, "c":100, "m":1000}
    return sum(map(lambda x: values[x], string))
