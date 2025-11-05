>>> from datetime import datetime, timedelta
>>> import humanize # $ pip install humanize
>>> humanize.naturaltime(datetime.now() - timedelta(days=1))
'a day ago'
>>> humanize.naturaltime(datetime.now() - timedelta(hours=2))
'2 hours ago'
