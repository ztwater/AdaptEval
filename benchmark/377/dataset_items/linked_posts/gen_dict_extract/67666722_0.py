import re

def search(dictionary, search_pattern, output=None):
    """
    Search nested dictionaries and lists using a regex search
    pattern to match a key and return the corresponding value(s).
    """
    if output is None:
        output = []

    pattern = re.compile(search_pattern)
    
    for k, v in dictionary.items():
        pattern_found = pattern.search(k)
        if not pattern_found:
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        search(item, search_pattern, output)
            if isinstance(v, dict):
                search(v, search_pattern, output)
        else:
            if pattern_found:
                output.append(v)

    return output
