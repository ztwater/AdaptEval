>>> import threading
>>> for i in range(50+1):
...   threading._sleep(0.5)
...   print "\r%3d" % i, ('='*i)+('-'*(50-i)),
