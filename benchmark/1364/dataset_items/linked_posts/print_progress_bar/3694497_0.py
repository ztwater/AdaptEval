import sys
def progresssbar():
         for i in range(100):
            time.sleep(1)
            sys.stdout.write("%i\r" % i)

progressbar()
