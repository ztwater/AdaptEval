import subprocess

command = "find {} -type d -empty -delete".format(folder_path)  
subprocess.run(command, shell=True)
