class Line:
    a = 19
    b = 4
    y = [a*x + b
         for a, b in [(a, b)]
         for x in range(10)]
