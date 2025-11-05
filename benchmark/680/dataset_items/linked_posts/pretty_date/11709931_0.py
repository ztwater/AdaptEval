from ago import human
from datetime import datetime
from datetime import timedelta

ts = datetime.now() - timedelta(days=1, hours=5)

print(human(ts))
# 1 day, 5 hours ago

print(human(ts, precision=1))
# 1 day ago
