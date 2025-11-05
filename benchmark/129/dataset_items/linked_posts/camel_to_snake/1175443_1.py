p = re.compile("([A-Z]+[a-z]+)([A-Z]?)")
print p.sub(lambda x: x.group(1).lower() + "_" + x.group(2).lower(), "CamelCase")
print p.sub(lambda x: x.group(1).lower() + "_" + x.group(2).lower(), "getHTTPResponseCode")
