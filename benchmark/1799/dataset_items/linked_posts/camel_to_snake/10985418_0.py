import re

def to_snake_case(camel_str):
    return re.sub('([A-Z0-9])', r'_\1', camel_str).lower().lstrip('_')
