import contextlib
import sys
import os

with contextlib.redirect_stdout(open(os.devnull, 'w')):
    sys.stdout.write("will not print")

sys.stdout.write("this will print")
