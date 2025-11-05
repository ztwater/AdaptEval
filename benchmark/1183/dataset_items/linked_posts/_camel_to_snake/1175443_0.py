def f(s):
    return s.group(1).lower() + "_" + s.group(2).lower()

p = re.compile("([A-Z]+[a-z]+)([A-Z]?)")
print p.sub(f, "CamelCase")
print p.sub(f, "getHTTPResponseCode")
