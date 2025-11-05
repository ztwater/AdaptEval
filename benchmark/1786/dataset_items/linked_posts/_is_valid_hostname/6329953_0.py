def is_valid_host(host):
    '''IDN compatible domain validator'''
    host = host.encode('idna').lower()
    if not hasattr(is_valid_host, '_re'):
        import re
        is_valid_host._re = re.compile(r'^([0-9a-z][-\w]*[0-9a-z]\.)+[a-z0-9\-]{2,15}$')
    return bool(is_valid_host._re.match(host))
