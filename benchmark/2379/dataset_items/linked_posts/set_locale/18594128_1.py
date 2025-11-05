#! /usr/bin/python3
import time
import locale
import contextlib

@contextlib.contextmanager
def setlocale(*args, **kw):
  saved = locale.setlocale(locale.LC_ALL)
  yield locale.setlocale(*args, **kw)
  locale.setlocale(locale.LC_ALL, saved)

def get_c_locale_abbrev():
  with setlocale(locale.LC_TIME, "C"):
    return time.strftime("%a-%b")

# Let's suppose that we're french
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

# Should print french, english, then french
print(time.strftime('%a-%b'))
print(get_c_locale_abbrev())
print(time.strftime('%a-%b'))
