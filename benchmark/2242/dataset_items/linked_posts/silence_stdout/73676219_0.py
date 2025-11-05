from io import StringIO
...
with StringIO() as out:
    with stdout_redirected(out):
        # Do your thing
