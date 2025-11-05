from itertools import islice

list_ = [i for i in range(10, 100)]

def chunker(it, size):
    iterator = iter(it)
    while chunk := list(islice(iterator, size)):
        print(chunk)
