def get_domain_suffixes():
    import requests
    res=requests.get('https://publicsuffix.org/list/public_suffix_list.dat')
    lst=set()
    for line in res.text.split('\n'):
        if not line.startswith('//'):
            domains=line.split('.')
            cand=domains[-1]
            if cand:
                lst.add('.'+cand)
    return tuple(sorted(lst))

domain_suffixes=get_domain_suffixes()

def reminds_url(txt:str):
    """
    >>> reminds_url('yandex.ru.com/somepath')
    True
    
    """
    ltext=txt.lower().split('/')[0]
    return ltext.startswith(('http','www','ftp')) or ltext.endswith(domain_suffixes)
