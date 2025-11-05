import os

print len(os.walk('/usr/lib').next()[2])
