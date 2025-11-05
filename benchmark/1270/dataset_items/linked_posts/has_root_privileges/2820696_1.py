$ cat apt.py
import errno
import subprocess

def get_install(package):
    cmd = '/usr/bin/apt-get install'.split()
    cmd.append(package)
    output_kw = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    p = subprocess.Popen(cmd, **output_kw)
    status = p.wait()
    error = p.stderr.read().lower()
    if status and 'permission denied' in error:
        raise OSError(errno.EACCES, 'Permission denied running apt-get')
    # other conditions here as you require
$ python
>>> import apt
>>> apt.get_install('python')
Traceback ...
OSError: [Errno 13] Permission denied running apt-get
