from math import sqrt, ceil

for i in range(1,10):
   thelen = (i * (i+1)) / 2
   thedim = sqrt(2*thelen + ceil(sqrt(2*thelen)))
   print "compressed array of length %d has dimension %d" % (thelen, thedim)
