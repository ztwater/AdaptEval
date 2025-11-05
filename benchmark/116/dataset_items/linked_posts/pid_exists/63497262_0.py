import os
import subprocess
import platform
import re

def pid_alive(pid:int):
    """ Check For whether a pid is alive """


    system = platform.uname().system
    if re.search('Linux', system, re.IGNORECASE):
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        else:
            return True
    elif re.search('Windows', system, re.IGNORECASE):
        out = subprocess.check_output(["tasklist","/fi",f"PID eq {pid}"]).strip()
        # b'INFO: No tasks are running which match the specified criteria.'

        if re.search(b'No tasks', out, re.IGNORECASE):
            return False
        else:
            return True
    else:
        raise RuntimeError(f"unsupported system={system}")
