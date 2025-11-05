import time
import sys

for i in range(101):
    time.sleep(0.05)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()
