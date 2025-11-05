"-".join(x.group(1).lower() for x in re.finditer("(^[^A-Z]+|[A-Z][^A-Z]+)", "stringToSplit"))
