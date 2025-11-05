import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser()
parser.add_argument("--my_bool", type=str, default="False")
args = parser.parse_args()

if bool(strtobool(args.my_bool)) is True:
    print("OK")
