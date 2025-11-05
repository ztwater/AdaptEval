import iteration_utilities
import itertools
from itertools import zip_longest

def consume_all(it):
    return iteration_utilities.consume(it, None)

import simple_benchmark
b = simple_benchmark.BenchmarkBuilder()

@b.add_function()
def grouper(l, n):
    return consume_all(iteration_utilities.grouper(l, n))

def Craz_inner(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

@b.add_function()
def Craz(iterable, n, fillvalue=None):
    return consume_all(Craz_inner(iterable, n, fillvalue))

def nosklo_inner(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

@b.add_function()
def nosklo(seq, size):
    return consume_all(nosklo_inner(seq, size))

def SLott_inner(ints, chunk_size):
    for i in range(0, len(ints), chunk_size):
        yield ints[i:i+chunk_size]

@b.add_function()
def SLott(ints, chunk_size):
    return consume_all(SLott_inner(ints, chunk_size))

def MarkusJarderot1_inner(iterable,size):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it,size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it,size))

@b.add_function()
def MarkusJarderot1(iterable,size):
    return consume_all(MarkusJarderot1_inner(iterable,size))

def MarkusJarderot2_inner(iterable,size,filler=None):
    it = itertools.chain(iterable,itertools.repeat(filler,size-1))
    chunk = tuple(itertools.islice(it,size))
    while len(chunk) == size:
        yield chunk
        chunk = tuple(itertools.islice(it,size))

@b.add_function()
def MarkusJarderot2(iterable,size):
    return consume_all(MarkusJarderot2_inner(iterable,size))

@b.add_arguments()
def argument_provider():
    for exp in range(2, 20):
        size = 2**exp
        yield size, simple_benchmark.MultiArgument([[0] * size, 10])

r = b.run()
