import os
import sys
oldstdout = os.dup(1)
oldstderr = os.dup(2)
oldsysstdout = sys.stdout
oldsysstderr = sys.stderr

# Cancel all stdout outputs (will be lost) - optionally also cancel stderr
def cancel_stdout(stderr=False):
    sys.stdout.flush()
    devnull = open('/dev/null', 'w')
    os.dup2(devnull.fileno(), 1)
    sys.stdout = devnull
    if stderr:
        os.dup2(devnull.fileno(), 2)
        sys.stderr = devnull

# Redirect all stdout outputs to a file - optionally also redirect stderr
def reroute_stdout(filepath, stderr=False):
    sys.stdout.flush()
    file = open(filepath, 'w')
    os.dup2(file.fileno(), 1)
    sys.stdout = file
    if stderr:
        os.dup2(file.fileno(), 2)
        sys.stderr = file

# Restores stdout to default - and stderr
def restore_stdout():
    sys.stdout.flush()
    sys.stdout.close()
    os.dup2(oldstdout, 1)
    os.dup2(oldstderr, 2)
    sys.stdout = oldsysstdout
    sys.stderr = oldsysstderr
