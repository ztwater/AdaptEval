def isValidHostname(hostname):
    disallowed = re.compile("[^a-zA-Z\d\-]")
    return all(map(lambda x: len(x) and not disallowed.search(x), hostname.split(".")))
