import argparse
from ast import parse
import sys
parser = argparse.ArgumentParser(description='')
parser.add_argument('--csv', action='store_true', default = False 
,help='read from csv')
args = parser.parse_args()

if args.csv:
    print('reading from csv')
