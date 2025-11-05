l = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 4
filler = 0
fills = len(l) % n
chunks = ((l + [filler] * fills)[x * n:x * n + n] for x in range(int((len(l) + n - 1)/n)))
print(chunks)

[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0]]
