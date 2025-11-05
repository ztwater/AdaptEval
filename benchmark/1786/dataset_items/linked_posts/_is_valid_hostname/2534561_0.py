
def isValidHostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname.endswith("."): # A single trailing dot is legal
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    disallowed = re.compile("[^A-Z\d-]", re.IGNORECASE)
    return all( # Split by labels and verify individually
        (label and len(label) <= 63 # length is within proper range
         and not label.startswith("-") and not label.endswith("-") # no bordering hyphens
         and not disallowed.search(label)) # contains only legal characters
        for label in hostname.split("."))
