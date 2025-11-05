import unicodedata

def neutralize_unicode(value):
    """
    Taking care of special characters as gently as possible

    Args:
        value (string): input string, can contain unicode characters

    Returns:
        :obj:`string` where the unicode characters are replaced with standard
        ASCII counterparts (for example en-dash and em-dash with regular dash,
        apostrophe and quotation variations with the standard ones) or taken
        out if there's no substitute.
    """
    if not value or not isinstance(value, basestring):
        return value

    if isinstance(value, str):
        return value

    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore")
