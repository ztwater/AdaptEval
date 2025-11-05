import inspect

def f1(): f2()

def f2():
    print ('caller name:', inspect.stack()[1][3])

f1()
