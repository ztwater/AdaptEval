>>> apt_get = ['/usr/bin/apt-get', 'install', 'python']
>>> p = subprocess.Popen(apt_get, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> p.wait()
100                 # Houston, we have a problem.
>>> p.stderr.read()
'E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)'
'E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?\n'
