>>> re.findall("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "CamelCaseXYZ")
['', '']
