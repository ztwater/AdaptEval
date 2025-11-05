import os, subprocess

def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if prompt_sudo() != 0:
    # the user wasn't authenticated as a sudoer, exit?
