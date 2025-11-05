def chunks(items, binsize):
    consumed = [0]
    sent = [0]
    it = iter(items)

    def g():
        c = 0
        while c < binsize:
            try:
                val = next(it)
            except StopIteration:
                sent[0] = None
                return
            consumed[0] += 1
            yield val
            c += 1

    while consumed[0] <= sent[0]:
        if consumed[0] < sent[0]:
            raise Exception("Cannot traverse a chunk before the previous is consumed.", consumed[0], sent[0])
        yield g()
        if sent[0] is None:
            return
        sent[0] += binsize


def g():
    for item in [1, 2, 3, 4, 5, 6, 7]:
        sleep(1)
        print(f"accessed:{item}→\t", end="")
        yield item


for chunk in chunks(g(), 3):
    for x in chunk:
        print(f"x:{x}\t\t\t", end="")
    print()

"""
Output:

accessed:1→ x:1         accessed:2→ x:2         accessed:3→ x:3         
accessed:4→ x:4         accessed:5→ x:5         accessed:6→ x:6         
accessed:7→ x:7 
"""
