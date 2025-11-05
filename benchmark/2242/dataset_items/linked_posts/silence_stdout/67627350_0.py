import argparse
import contextlib

class NonWritable:
    def write(self, *args, **kwargs):
        pass

parser = argparse.ArgumentParser(description='my program')
parser.add_argument("-p", "--param", help="my parameter", type=str, required=True)

#with contextlib.redirect_stdout(None): # No effect as `argparse` will output to `stderr`
#with contextlib.redirect_stderr(None): # AttributeError: 'NoneType' object has no attribute 'write'
with contextlib.redirect_stderr(NonWritable): # this works!
    args = parser.parse_args()
