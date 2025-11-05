import itertools
import sys

def windowed(l, stride):
    return zip(*[itertools.islice(l, i, sys.maxsize) for i in range(stride)])
