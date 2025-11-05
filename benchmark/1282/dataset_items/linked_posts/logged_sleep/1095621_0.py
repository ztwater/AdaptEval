import inspect 

def info(msg):
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    print '[%s] %s' % (mod.__name__, msg)
