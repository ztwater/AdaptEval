from collections import namedtuple

# module parameter added in python 3.6
namespace = namedtuple("namespace", "foo bar", module=__name__ + ".namespace")
