filter_namespace = argparse.Namespace(filter1=None, filter2=None)
namespace = argparse.Namespace(filter=filter_namespace)
namespace = main_parser.parse_args(namespace=namespace)
