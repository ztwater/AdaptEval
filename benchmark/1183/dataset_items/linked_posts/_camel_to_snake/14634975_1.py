"-".join(x.group(1).lower() if x.group(2) is None else x.group(1) \
         for x in re.finditer("((^.[^A-Z]+)|([A-Z][^A-Z]+))", "stringToSplit"))
