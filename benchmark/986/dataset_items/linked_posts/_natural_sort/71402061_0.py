def string_to_pairs(s, pairs=re.compile(r"(\D*)(\d*)").findall):
    return [(text.lower(), int(digits or 0)) for (text, digits) in pairs(s)[:-1]]
