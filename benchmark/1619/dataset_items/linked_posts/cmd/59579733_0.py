from distutils.util import strtobool

parser.add_argument('--feature', dest='feature', 
                    type=lambda x: bool(strtobool(x)))
