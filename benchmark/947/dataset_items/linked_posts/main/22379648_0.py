import argparse
parser = argparse.ArgumentParser(description="Prepare something code.")
parser.add_argument("type", choices=("tabular", "verbose", "t", "v"))
args = parser.parse_args()
if args.type in ("tabular", "t"):
    print "Tabular print"
else:  # Must be "verbose" or "v"
    print "VERBOSE"
