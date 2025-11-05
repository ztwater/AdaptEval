import re
def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    hostname = hostname.rstrip(".")
    allowed = re.compile("(?!-)[A-Z\d\-\_]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

# convert your unicode hostname to punycode (python 3 ) 
# Remove the port number from hostname
normalise_host = hostname.encode("idna").decode().split(":")[0]
is_valid_hostname(normalise_host )
