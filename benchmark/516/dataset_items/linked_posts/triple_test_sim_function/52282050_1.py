from subprocess import check_call
try:
    check_call(['mkdir', '-p', 'path1/path2/path3'])
except:
    handle...
