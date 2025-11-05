def camel_case_split(identifier):
    matches = finditer('(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', identifier)
    split_string = []
    # index of beginning of slice
    previous = 0
    for match in matches:
        # get slice
        split_string.append(identifier[previous:match.start()])
        # advance index
        previous = match.start()
    # get remaining string
    split_string.append(identifier[previous:])
    return split_string
