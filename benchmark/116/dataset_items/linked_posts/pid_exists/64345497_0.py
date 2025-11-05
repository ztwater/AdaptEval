import psutil
import subprocess
import os
p = subprocess.Popen(['python', self.evaluation_script],stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 

pid = p.pid

def __check_process_running__(self,p):
    if p is not None:
        poll = p.poll()
        if poll == None:
            return True
    return False
    
def __check_PID_running__(self,pid):
    """
        Checks if a pid is still running (UNIX works, windows we'll see)
        Inputs:
            pid - process id
        returns:
            True if running, False if not
    """
    if (platform.system() == 'Linux'):
        try:
            os.kill(pid, 0)
            if pid<0:               # In case code terminates
                return False
        except OSError:
            return False 
        else:
            return True
    elif (platform.system() == 'Windows'):
        return pid in (p.pid for p in psutil.process_iter())
