import datetime as dt

def human_time_ago(now: dt.datetime, past: dt.datetime) -> str:
    """Return time difference as human-readable string"""
    periods = (
        ("year", 60 * 60 * 24 * 365),
        ("month", 60 * 60 * 24 * 30),
        ("week", 60 * 60 * 24 * 7),
        ("day", 60 * 60 * 24),
        ("hour", 60 * 60),
        ("minute", 60),
    )
    diff = now - past

    for period, seconds_each in periods:
        if diff.total_seconds() >= seconds_each:
            how_many = int(diff.total_seconds() / seconds_each)
            return f"{how_many} {period}{'s' if how_many >= 2 else ''} ago"

    return "just now"  # less than a minute ago
