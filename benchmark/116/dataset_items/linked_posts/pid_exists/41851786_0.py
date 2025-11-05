import os

def is_running(pid):
    if os.path.isdir('/proc/{}'.format(pid)):
        return True
    return False
