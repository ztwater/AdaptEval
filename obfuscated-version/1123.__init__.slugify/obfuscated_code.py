def slugify(var_0, var_1=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    var_0 = str(var_0)
    if var_1:
        var_0 = unicodedata.normalize('NFKC', var_0)
    else:
        var_0 = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    var_0 = re.sub(r'[^\w\s-]', '', var_0.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')
