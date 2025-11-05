from timeout import timeout

# Timeout a long running function with the default expiry of 10 seconds.
@timeout
def long_running_function1():
    ...

# Timeout after 5 seconds
@timeout(5)
def long_running_function2():
    ...

# Timeout after 30 seconds, with the error "Connection timed out"
@timeout(30, os.strerror(errno.ETIMEDOUT))
def long_running_function3():
    ...
