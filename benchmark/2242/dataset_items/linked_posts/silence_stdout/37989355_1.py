import contextlib

with contextlib.redirect_stdout(None):
    print("will not print")

print("this will print")
