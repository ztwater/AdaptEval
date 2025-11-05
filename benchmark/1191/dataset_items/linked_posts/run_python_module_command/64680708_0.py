import subprocess
ls = subprocess.run(['ls', '-a'], capture_output=True, text=True).stdout.strip("\n")
print(ls)
