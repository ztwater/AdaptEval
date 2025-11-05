import subprocess
path = "your path here"
command = ["find", path, "-type", "d", "-empty", "-delete"]
subprocess.run(command)
