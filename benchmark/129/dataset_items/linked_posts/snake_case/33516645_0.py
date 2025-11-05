import re

def convert(name):
    return re.sub(r'([A-Z]*)([A-Z][a-z]+)', lambda x: (x.group(1) + '_' if x.group(1) else '') + x.group(2) + '_', name).rstrip('_').lower()
