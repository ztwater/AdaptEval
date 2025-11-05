from datetime import datetime

def pretty_date(time, now=None):
    """Convert a datetime or timestamp to a pretty, relative date.

    Args:
        time (datetime.datetime or int): date to print prettily
        now (datetime.datetime): datetime for 'now', i.e. the date the pretty date
            is relative to (default is datetime.now())

    Returns:
        (str): pretty string like 'an hour ago', 'Yesterday',
            '3 months ago', 'just now', etc.

    Adapted from https://stackoverflow.com/questions/1551382.

    """
    if now is None:
        now = datetime.now()

    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    else:
        raise ValueError("pretty_date requires a timestamp or datetime")

    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''
        
    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 28:
        weeks = day_diff // 7
        if weeks == 1:
            return "a week ago"
        else:
            return str(day_diff // 7) + " weeks ago"
    
    if day_diff < 365:
        months = day_diff // 30
        if months == 1:
            return "a month ago"
        elif months == 12:
            months -= 1
        return str(months) + " months ago"

    diff = day_diff // 365
    
    if diff == 1:
        return "a year ago"
    else:
        return str(diff) + " years ago"
