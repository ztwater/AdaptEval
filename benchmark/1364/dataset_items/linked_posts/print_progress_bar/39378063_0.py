import sys
import time

max_length = 5
at_length = max_length
empty = "-"
used = "%"

bar = empty * max_length

for i in range(0, max_length):
    at_length -= 1

    #setting empty and full spots
    bar = used * i
    bar = bar+empty * at_length

    #\r is carriage return(sets cursor position in terminal to start of line)
    #\0 character escape

    sys.stdout.write("[{}]\0\r".format(bar))
    sys.stdout.flush()

    #do your stuff here instead of time.sleep
    time.sleep(1)

sys.stdout.write("\n")
sys.stdout.flush()
