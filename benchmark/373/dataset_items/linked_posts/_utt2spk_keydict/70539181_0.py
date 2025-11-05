import argparse

parser = argparse.ArgumentParser(
    description='test', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-g', choices=['a', 'b', 'g', 'd', 'e'], default='a',
                    help=('Some option, where\n'
                          ' a = alpha\n'
                          ' b = beta\n'
                          ' g = gamma\n'
                          ' d = delta\n'
                          ' e = epsilon'))

parser.parse_args()

