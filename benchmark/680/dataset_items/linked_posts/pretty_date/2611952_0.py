from datetime import datetime, timedelta
now = datetime.now()
hrago = now - timedelta(hours=1)
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
dayafter = now + timedelta(days=2)

import pretty
print pretty.date(now)                      # 'now'
print pretty.date(hrago)                    # 'an hour ago'
print pretty.date(hrago, short=True)        # '1h ago'
print pretty.date(hrago, asdays=True)       # 'today'
print pretty.date(yesterday, short=True)    # 'yest'
print pretty.date(tomorrow)                 # 'tomorrow'
