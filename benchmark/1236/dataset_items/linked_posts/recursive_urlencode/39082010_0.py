#!/usr/bin/env python3

import urllib.parse

def http_build_query(data):
    parents = list()
    pairs = dict()

    def renderKey(parents):
        depth, outStr = 0, ''
        for x in parents:
            s = "[%s]" if depth > 0 or isinstance(x, int) else "%s"
            outStr += s % str(x)
            depth += 1
        return outStr

    def r_urlencode(data):
        if isinstance(data, list) or isinstance(data, tuple):
            for i in range(len(data)):
                parents.append(i)
                r_urlencode(data[i])
                parents.pop()
        elif isinstance(data, dict):
            for key, value in data.items():
                parents.append(key)
                r_urlencode(value)
                parents.pop()
        else:
            pairs[renderKey(parents)] = str(data)

        return pairs
    return urllib.parse.urlencode(r_urlencode(data))

if __name__ == '__main__':
    payload = {
        'action': 'add',
        'controller': 'invoice',
        'code': 'debtor',
        'InvoiceLines': [
            {'PriceExcl': 150, 'Description': 'Setupfee'},
            {'PriceExcl':49.99, 'Description':'Subscription'}
        ],
        'date': '2016-08-01',
        'key': 'Yikes&ampersand'
    }
    print(http_build_query(payload))

    payload2 = [
        'item1',
        'item2'
    ]
    print(http_build_query(payload2))
