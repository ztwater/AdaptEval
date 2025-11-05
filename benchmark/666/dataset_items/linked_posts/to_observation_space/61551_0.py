dict((key, value) for key, value in f.__dict__.iteritems() 
    if not callable(value) and not key.startswith('__'))
