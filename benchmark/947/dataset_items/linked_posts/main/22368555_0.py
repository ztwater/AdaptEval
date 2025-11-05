import argparse
parser = argparse.ArgumentParser(description="Prepare something code.")
parser.add_argument("-t","--tabular", help="print something in tabular way for EXCEL",
                      action="store_true")
parser.add_argument("-v","--verbose", action="store_true")
args = parser.parse_args()
if args.tabular:
    print "Tabular print"
elif args.verbose:
    print "VERBOSE"
else:
    print parser.print_help()
