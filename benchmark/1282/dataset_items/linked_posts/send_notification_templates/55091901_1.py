for i in range(3):
    def f(i=i):  # <- right here is the important bit
        return i

    functions.append(f)
