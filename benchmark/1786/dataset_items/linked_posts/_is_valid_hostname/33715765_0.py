import re

def validate_fqdn(dn):
    if dn.endswith('.'):
        dn = dn[:-1]
    if len(dn) < 1 or len(dn) > 253:
        return False
    ldh_re = re.compile('^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$',
                        re.IGNORECASE)
    return all(ldh_re.match(x) for x in dn.split('.'))
