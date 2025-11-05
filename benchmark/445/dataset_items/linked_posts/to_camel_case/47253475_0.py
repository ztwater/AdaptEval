import re

def snake_to_camel(text):
    return re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).upper(), text)
