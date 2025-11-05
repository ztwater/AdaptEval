def un_camel(text):
    """ Converts a CamelCase name into an under_score name. 

        >>> un_camel('CamelCase')
        'camel_case'
        >>> un_camel('getHTTPResponseCode')
        'get_http_response_code'
    """
    result = []
    pos = 0
    while pos < len(text):
        if text[pos].isupper():
            if pos-1 > 0 and text[pos-1].islower() or pos-1 > 0 and \
            pos+1 < len(text) and text[pos+1].islower():
                result.append("_%s" % text[pos].lower())
            else:
                result.append(text[pos].lower())
        else:
            result.append(text[pos])
        pos += 1
    return "".join(result)
