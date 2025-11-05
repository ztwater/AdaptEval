import os
import sys
from contextlib import contextmanager

@contextmanager
def silence_stdout():
    old_target = sys.stdout
    try:
        with open(os.devnull, "w") as new_target:
            sys.stdout = new_target
            yield new_target
    finally:
        sys.stdout = old_target

with silence_stdout():
    print("will not print")

print("this will print")
