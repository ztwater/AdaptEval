import os, sys, msvcrt

msvcrt.setmode (sys.stdin.fileno(), os.O_BINARY)
s = sys.stdin.read()
print len (s)
