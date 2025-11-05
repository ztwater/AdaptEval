def get_encoded_url_params(d):
    """URL-encode a nested dictionary.
    :param d = dict
    :returns url encoded string with dict key-value pairs as query parameters
    e.g.
    if d = { "addr":{ "country": "US", "line": ["a","b"] },
            "routing_number": "011100915", "token": "asdf"
        }
    :returns 'addr[country]=US&addr[line][0]=a&addr[line][1]=b&routing_number=011100915&token=asdf'
    or 'addr%5Bcountry%5D=US&addr%5Bline%5D%5B0%5D=a&addr%5Bline%5D%5B1%5D=b&routing_number=011100915&token=asdf'
    (which is url encoded form of the former using quote_plus())
    """

    def get_pairs(value, base):
        if isinstance(value, dict):
            return get_dict_pairs(value, base)
        elif isinstance(value, list):
            return get_list_pairs(value, base)
        else:
            return [base + '=' + str(value)]
            # use quote_plus() to get url encoded string
            # return [quote_plus(base) + '=' + quote_plus(str(value))]

    def get_list_pairs(li, base):
        pairs = []
        for idx, value in enumerate(li):
            new_base = base + '[' + str(idx) + ']'
            pairs += get_pairs(value, new_base)
        return pairs

    def get_dict_pairs(d, base=''):
        pairs = []
        for key, value in d.items():
            new_base = key if base == '' else base + '[' + key + ']'
            pairs += get_pairs(value, new_base)
        return pairs

    return '&'.join(get_dict_pairs(d))
