import re

def _camel_to_snake(name):
    """Convert from CamelCase to snake_case"""

    # Adapted from https://stackoverflow.com/a/1176023
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    name = name.lower()
    return name
