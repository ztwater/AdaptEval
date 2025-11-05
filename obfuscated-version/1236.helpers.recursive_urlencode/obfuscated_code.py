import urllib

def recursive_urlencode(var_0):
    """URL-encode a multidimensional dictionary.

    >>> data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
    >>> recursive_urlencode(data)
    u'a=b%26c&j=k&d[e][f%26g]=h%2Ai'
    """
    def recursion(var_0, var_1=[]):
        var_2 = []

        for key, value in var_0.items():
            var_3 = var_1 + [key]
            if hasattr(value, 'values'):
                var_2 += recursion(value, var_3)
            else:
                var_4 = None
                if len(var_3) > 1:
                    var_5 = urllib.quote(var_3.pop(0))
                    var_6 = map(lambda x: urllib.quote(x), var_3)
                    var_4 = "%s[%s]=%s" % (var_5, ']['.join(var_6), urllib.quote(unicode(value)))
                else:
                    var_4 = "%s=%s" % (urllib.quote(unicode(key)), urllib.quote(unicode(value)))
                var_2.append(var_4)
        return var_2

    return '&'.join(recursion(var_0))

