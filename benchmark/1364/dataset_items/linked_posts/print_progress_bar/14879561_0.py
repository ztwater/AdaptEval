import os
import time
def load(left_side, right_side, length, time):
    x = 0
    y = ""
    print "\r"
    while x < length:
        space = length - len(y)
        space = " " * space
        z = left + y + space + right
        print "\r", z,
        y += "█"
        time.sleep(time)
        x += 1
    cls()
