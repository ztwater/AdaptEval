import itertools    

def batch_generator(iterable, batch_size=1):
    iterable = iter(iterable)

    while True:
        batch = list(itertools.islice(iterable, batch_size))
        if len(batch) > 0:
            yield batch
        else:
            break

for x in batch_generator(range(0, 10), 3):
    print(x)
