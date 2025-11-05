import locale
import threading

from datetime import datetime
from contextlib import contextmanager


LOCALE_LOCK = threading.Lock()

@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

# Let's set a non-US locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

# Example to write a formatted English date
with setlocale('C'):
    print(datetime.now().strftime('%a, %b')) # e.g. => "Thu, Jun"

# Example to read a formatted English date
with setlocale('C'):
    mydate = datetime.strptime('Thu, Jun', '%a, %b')
