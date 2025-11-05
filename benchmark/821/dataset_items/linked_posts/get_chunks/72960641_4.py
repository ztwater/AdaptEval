from timeit import repeat

setup = """
import itertools
import more_itertools as mit


def cottontail(lst, n):
    for tup in zip(*[iter(lst)]*n): tup
    rest = tuple(lst[len(lst)//n*n: ])
    if rest: rest

def it_batched(it, n):
    for x in itertools.batched(it, n): x

def NedBatchelder(lst, n):
    for i in range(0, len(lst), n): lst[i:i + n]

def pylang1(iterable, n):
    for x in mit.chunked(iterable, n): x

def senderle(it, size):
    it = iter(it)
    for x in iter(lambda: tuple(itertools.islice(it, size)), ()): x

def nirvana_msu(iterable, size):
    it = iter(iterable)
    while item := list(itertools.islice(it, size)):
        item

lst = list(range(1_000_000))
"""

out = {}
for f in ("NedBatchelder", "pylang1", "senderle", 
          "nirvana_msu", "cottontail", "it_batched"):
    for k in (3, 910):
        tm = min(repeat(f"{f}(lst, {k})", setup, number=100))
        out.setdefault(f, {})[k] = tm*10
out = dict(sorted(out.items(), key=lambda xy: xy[1][3]))

print('    Chunk size         3      910\nFunctions')
for func, val in out.items():
    print("{:<15}  {:>5.1f}ms  {:>5.1f}ms".format(func, val[3], val[910]))
