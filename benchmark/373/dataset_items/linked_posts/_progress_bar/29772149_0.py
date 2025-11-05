import time,sys

for i in range(100+1):
    time.sleep(0.1)
    sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
    sys.stdout.flush()
