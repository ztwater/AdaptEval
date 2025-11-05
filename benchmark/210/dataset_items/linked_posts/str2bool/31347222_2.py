feature_parser = parser.add_mutually_exclusive_group(required=False)
feature_parser.add_argument('--feature', dest='feature', action='store_true')
feature_parser.add_argument('--no-feature', dest='feature', action='store_false')
parser.set_defaults(feature=True)
