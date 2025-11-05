#!/usr/bin/env python
import inspect

called=lambda: inspect.stack()[1][3]

def caller1():
    print "inside: ",called()

def caller2():
    print "inside: ",called()
    
if __name__=='__main__':
    caller1()
    caller2()
