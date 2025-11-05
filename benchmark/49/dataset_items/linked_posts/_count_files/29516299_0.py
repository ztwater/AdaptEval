import os
import subprocess

def get_num_files(path):
    cmd = 'DIR \"%s\" /A-D /B /S | FIND /C /V ""' % path
    return int(subprocess.check_output(cmd, shell=True))
