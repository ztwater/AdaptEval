# -*- coding: utf-8 -*-
import yaml

def should_use_block(value):
    for c in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2028\u2029":
        if c in value:
            return True
    return False

def my_represent_scalar(self, tag, value, style=None):
    if style is None:
        if should_use_block(value):
             style='|'
        else:
            style = self.default_style

    node = yaml.representer.ScalarNode(tag, value, style=style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    return node


a={'short': "Hello", 'multiline': """Line1
Line2
Line3
""", 'multiline-unicode': u"""Lêne1
Lêne2
Lêne3
"""}

print(yaml.dump(a))
print(yaml.dump(a, allow_unicode=True))
yaml.representer.BaseRepresenter.represent_scalar = my_represent_scalar
print(yaml.dump(a))
print(yaml.dump(a, allow_unicode=True))
