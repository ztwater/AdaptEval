import contextlib

with contextlib.redirect_stdout(None):
  print("This won't print!")
