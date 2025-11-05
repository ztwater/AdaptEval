import subprocess
import shlex

sp_ls = subprocess.Popen(shlex.split(r'ls -l'), stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
sp_sed = subprocess.Popen(shlex.split(r'sed "s/a/b/g"'), stdin = sp_ls.stdout, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
sp_ls.stdin.close() # makes it similiar to /dev/null
output = sp_ls.communicate()[0] # which makes you ignore any errors.
print output
