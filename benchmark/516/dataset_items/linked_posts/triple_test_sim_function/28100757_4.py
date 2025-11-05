import errno
try:
    with open(filepath) as my_file:
        do_stuff(my_file)
except IOError as error:
    if error.errno == errno.ENOENT:
        print 'ignoring error because directory or file is not there'
    else:
        raise
