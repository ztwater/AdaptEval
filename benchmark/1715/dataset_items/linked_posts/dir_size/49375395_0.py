import subprocess
import os

#
# get folder size
#
def get_size(self, path):
    if os.path.exists(path) and path != '/':
        cmd = str(subprocess.check_output(['sudo', 'du', '-s', path])).\
            replace('b\'', '').replace('\'', '').split('\\t')[0]
        return float(cmd) / 1000000
    elif os.path.exists(path) and path == '/':
        cmd = str(subprocess.getoutput(['sudo du -s /'])). \
            replace('b\'', '').replace('\'', '').split('\n')
        val = cmd[len(cmd) - 1].replace('/', '').replace(' ', '')
        return float(val) / 1000000
    else: raise ValueError
