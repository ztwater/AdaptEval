import sys

def rogue_function():
    print('spam to stdout')
    print('important warning', file=sys.stderr)
    1 + 'a'
    return 42

with suppress_stdout_stderr():
    rogue_function()
