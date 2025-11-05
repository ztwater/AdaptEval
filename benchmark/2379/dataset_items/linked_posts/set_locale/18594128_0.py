#! /usr/bin/python3
import time
import locale


def get_c_locale_abbrev():
  lc = locale.setlocale(locale.LC_TIME)
  try:
    locale.setlocale(locale.LC_TIME, "C")
    return time.strftime("%a-%b")
  finally:
    locale.setlocale(locale.LC_TIME, lc)

# Let's suppose that we're french
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

# Should print french, english, then french
print(time.strftime('%a-%b'))
print(get_c_locale_abbrev())
print(time.strftime('%a-%b'))
