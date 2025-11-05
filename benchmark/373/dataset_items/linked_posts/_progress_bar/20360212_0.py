import time
for i in range(100):
    time.sleep(1)
    s = "{}% Complete".format(i)
    print(s,end=len(s) * '\b')
