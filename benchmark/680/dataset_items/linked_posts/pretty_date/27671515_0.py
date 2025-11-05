>>> from datetime import datetime
>>> from dateutil.relativedelta import relativedelta
>>> then = datetime(2003, 9, 17, 20, 54, 47, 282310)
>>> relativedelta(then, datetime.now())
relativedelta(years=-11, months=-3, days=-9, hours=-18, minutes=-17, seconds=-8, microseconds=+912664)
