def suppress_std(func):
    def wrapper(*args, **kwargs):
        stderr_tmp = sys.stderr
        stdout_tmp = sys.stdout
        null = open(os.devnull, 'w')
        sys.stdout = null
        sys.stderr = null
        try:
            result = func(*args, **kwargs)
            sys.stderr = stderr_tmp
            sys.stdout = stdout_tmp
            return result
        except:
            sys.stderr = stderr_tmp
            sys.stdout = stdout_tmp
            raise
    return wrapper
