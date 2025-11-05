import subprocess

def system_command(cmd):
    """"Function executes cmd parameter as a bash command."""
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    stdout, stderr = p.communicate()
    return stdout, stderr

size = int(system_command('du -sb . ')[0].split()[0])
