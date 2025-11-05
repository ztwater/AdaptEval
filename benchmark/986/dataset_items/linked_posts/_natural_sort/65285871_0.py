import re

def padzero_with_lower(s):
    return re.sub(r'\d+', lambda m: m.group(0).rjust(10, '0'), s).lower()
