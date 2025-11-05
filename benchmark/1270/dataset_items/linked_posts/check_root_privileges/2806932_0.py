import errno

try:
    os.rename('/etc/foo', '/etc/bar')
except IOError as e:
    if e[0] == errno.EPERM:
       sys.exit("You need root permissions to do this, laterz!")
