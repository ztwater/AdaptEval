def replace_all(dict, str):
    for key in dict:
        str = str.replace(key, dict[key])
    return str
