import sys
import ruamel.yaml

yaml_str = """\
- key_1: value_a
  key_2: value_b

- key_1: value_c
  key_2: value_d

- key_1: value_x  # a few before this were ellipsed
  key_2: value_y
"""

yaml = ruamel.yaml.YAML()
data = yaml.load(yaml_str)
yaml.dump(data, sys.stdout)
