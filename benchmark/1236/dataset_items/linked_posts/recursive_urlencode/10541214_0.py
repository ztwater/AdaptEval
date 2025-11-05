#!/usr/bin/env python

import sys
import urllib

def recursive_urlencode(data):
    def r_urlencode(data, parent=None, pairs=None):
        if pairs is None:
            pairs = {}
        if parent is None:
            parents = []
        else:
            parents = parent

        for key, value in data.items():
            if hasattr(value, 'values'):
                parents.append(key)
                r_urlencode(value, parents, pairs)
                parents.pop()
            else:
                pairs[renderKey(parents + [key])] = renderVal(value)

        return pairs
    return urllib.urlencode(r_urlencode(data))


def renderKey(parents):
    depth, outStr = 0, ''
    for x in parents:
        str = "[%s]" if depth > 0 else "%s"
        outStr += str % renderVal(x)
        depth += 1
    return outStr


def renderVal(val):
    return urllib.quote(unicode(val))


def main():
    print recursive_urlencode(payload)


if __name__ == '__main__':
    sys.exit(main())
