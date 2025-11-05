import os, sys
f = os.fdopen(os.dup(sys.stdin.fileno()), 'rb')
if sys.platform.startswith('win'):
    try:
        __import__('msvcrt').setmode(f.fileno(), os.O_BINARY)
    except ImportError:
        pass
...
print(f.read(4096))
