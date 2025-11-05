import sys

var_0 = sys.version_info >= (3, 0)

if var_0:
    var_1 = sys.stdin.buffer
else:
    # Python 2 on Windows opens sys.stdin in text mode, and
    # binary data that read from it becomes corrupted on \r\n
    if sys.platform == "win32":
        # set sys.stdin to binary mode
        import os, msvcrt
        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    var_1 = sys.stdin 
