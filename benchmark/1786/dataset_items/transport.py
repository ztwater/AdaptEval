"""Implementation of the QMI_Transport class."""
 
import re  
 

def _is_valid_hostname(hostname: str) -> bool:
    """Return True if the specified host name has valid syntax."""
    # source: https://stackoverflow.com/questions/2532053/validate-a-hostname-string
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # strip exactly one dot from the right, if present
    parts = hostname.split(".")
    if re.match(r"^[0-9]+$", parts[-1]):
        return False  # numeric TLD, not a domain name
    allowed = re.compile(r"(?!-)[A-Z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in parts)

