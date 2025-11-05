import sys
from ruamel.yaml import YAML

yaml_str = """\
short: "Hello"  # does keep the quotes, but need to tell the loader
long: |
  Line1
  Line2
  Line3
folded: >
  some like
  explicit folding
  of scalars
  for readability
"""

yaml = YAML()
yaml.preserve_quotes = True
data = yaml.load(yaml_str)
yaml.dump(data, sys.stdout)
