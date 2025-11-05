# jython
try:
    from java.lang import Runtime
    runtime = Runtime.getRuntime()
    res = runtime.availableProcessors()
    if res > 0:
        return res
except ImportError:
    pass
