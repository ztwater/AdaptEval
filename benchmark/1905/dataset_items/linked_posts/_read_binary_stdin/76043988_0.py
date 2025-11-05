import os, sys
if sys.platform.startswith('win'):
    try:
        __import__('msvcrt').setmode(sys.stdout.fileno(), os.O_BINARY)
    except ImportError:
        pass
sys.stdin = os.fdopen(sys.stdin.fileno(), 'rb')
...
print(sys.stdin.read(4096))
