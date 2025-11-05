import sys
from ruamel.yaml import YAML

yaml_str = """\
3: abc
conf:
    10: def
    3: gij     # h is missing
more:
- what
- else
"""

yaml = YAML()
data = yaml.load(yaml_str)
data['conf'][10] = 'klm'
data['conf'][3] = 'jig'
yaml.dump(data, sys.stdout)
