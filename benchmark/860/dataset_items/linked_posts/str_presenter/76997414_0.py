from ruamel.yaml import YAML
from io import StringIO

def yaml2dict(y):
    return YAML().load(y)

def dict2yaml(d):
    output_stream = StringIO()
    YAML().dump(d, output_stream)
    return output_stream.getvalue()
