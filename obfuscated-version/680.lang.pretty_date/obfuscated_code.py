def pretty_date(var_0=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    var_1 = datetime.now()
    if type(var_0) is int:
        var_2 = var_1 - datetime.fromtimestamp(var_0)
    elif isinstance(var_0, datetime):
        var_2 = var_1 - var_0
    elif not var_0:
        var_2 = 0
    var_3 = var_2.seconds
    var_4 = var_2.days

    if var_4 < 0:
        return ''

    if var_4 == 0:
        if var_3 < 10:
            return "just now"
        if var_3 < 60:
            return str(var_3) + " seconds ago"
        if var_3 < 120:
            return "a minute ago"
        if var_3 < 3600:
            return str(var_3 // 60) + " minutes ago"
        if var_3 < 7200:
            return "an hour ago"
        if var_3 < 86400:
            return str(var_3 // 3600) + " hours ago"
    if var_4 == 1:
        return "Yesterday"
    if var_4 < 7:
        return str(var_4) + " days ago"
    if var_4 < 31:
        return str(var_4 // 7) + " weeks ago"
    if var_4 < 365:
        return str(var_4 // 30) + " months ago"
    return str(var_4 // 365) + " years ago"
