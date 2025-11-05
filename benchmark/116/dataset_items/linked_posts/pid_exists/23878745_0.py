import subprocess

def running_process(process):
    "check if process is running. < process > is the name of the process."

    proc = subprocess.Popen(["if pgrep " + process + " >/dev/null 2>&1; then echo 'True'; else echo 'False'; fi"], stdout=subprocess.PIPE, shell=True)

    (Process_Existance, err) = proc.communicate()
    return Process_Existance

# use the function
print running_process("banshee")
