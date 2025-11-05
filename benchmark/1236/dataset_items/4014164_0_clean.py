import urllib

def recursive_urlencode(d):
    """URL-encode a multidimensional dictionary.

    >>> data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
    >>> recursive_urlencode(data)
    u'a=b%26c&j=k&d[e][f%26g]=h%2Ai'
    """
    def recursion(d, base=[]):
        pairs = []

        for key, value in d.items():
            new_base = base + [key]
            if hasattr(value, 'values'):
                pairs += recursion(value, new_base)
            else:
                new_pair = None
                if len(new_base) > 1:
                    first = urllib.quote(new_base.pop(0))
                    rest = map(lambda x: urllib.quote(x), new_base)
                    new_pair = "%s[%s]=%s" % (first, ']['.join(rest), urllib.quote(unicode(value)))
                else:
                    new_pair = "%s=%s" % (urllib.quote(unicode(key)), urllib.quote(unicode(value)))
                pairs.append(new_pair)
        return pairs

    return '&'.join(recursion(d))

