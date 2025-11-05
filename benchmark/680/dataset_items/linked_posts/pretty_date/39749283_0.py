>>> import arrow
>>> utc = arrow.utcnow()
>>> utc = utc.shift(hours=-1)
>>> utc.humanize()
'an hour ago'
