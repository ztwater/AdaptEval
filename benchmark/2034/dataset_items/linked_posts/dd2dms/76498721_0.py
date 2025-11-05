import sys
import math

dd = float(sys.argv[1])
f,d = math.modf(dd)
f,m = math.modf(60*f)
s = round(60*f, 6)

print(int(d), int(m), s)
