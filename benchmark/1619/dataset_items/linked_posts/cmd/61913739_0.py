import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser()
parser.add_argument("--foo", 
    type=lambda x:bool(strtobool(x)),
    nargs='?', const=True, default=False)
args = parser.parse_args()
print(args.foo)
