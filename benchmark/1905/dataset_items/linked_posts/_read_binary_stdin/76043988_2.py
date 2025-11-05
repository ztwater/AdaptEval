import os, sys
f = sys.stdin  # Or anything other file object.
if sys.platform.startswith('win'):
    try:
        __import__('msvcrt').setmode(f.fileno(), os.O_BINARY)
    except ImportError:
        pass
...
print(os.read(f.fileno(), 4096))
