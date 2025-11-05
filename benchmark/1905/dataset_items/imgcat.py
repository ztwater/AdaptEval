import os
import sys
 
def _read_binary_stdin():
    # see https://stackoverflow.com/a/38939320/474819 for other platform notes
    PY3 = sys.version_info >= (3, 0)
    if PY3:
        source = sys.stdin.buffer
    else:
        # Python 2 on Windows opens sys.stdin in text mode, and
        # binary data that read from it becomes corrupted on \r\n
        if sys.platform == "win32":
            # set sys.stdin to binary mode
            import msvcrt
            msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
        source = sys.stdin

    return source.read()
