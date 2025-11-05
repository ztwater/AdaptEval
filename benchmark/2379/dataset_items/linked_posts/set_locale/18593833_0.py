import pytz
UTC = pytz.timezone('UTC') # utc
fr = pytz.timezone('Europe/Paris') #your local
from datetime import datetime
date = datetime.now(fr)
dateUTC = date.astimezone(UTC)
