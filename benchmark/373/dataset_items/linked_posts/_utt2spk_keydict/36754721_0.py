import argparse, textwrap
parser = argparse.ArgumentParser(description='some information',
        usage='use "python %(prog)s --help" for more information',
        formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--argument', default=somedefault, type=sometype,
        help= textwrap.dedent('''\
        First line
        Second line
        More lines ... '''))
