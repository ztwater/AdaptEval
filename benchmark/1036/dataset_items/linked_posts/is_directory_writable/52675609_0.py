#! /usr/bin/env python
import os
import argparse

def writable_dir(dir):
    if os.access(dir, os.W_OK) and os.path.isdir(dir):
        return os.path.abspath(dir)
    else:
        raise argparse.ArgumentTypeError(dir + " is not writable or does not exist.")

parser = argparse.ArgumentParser()
parser.add_argument("-d","--dir", type=writable_dir, default='/tmp/',
    help="Directory to use. Default: /tmp")
opts = parser.parse_args()
