import subprocess

try:
        q = subprocess.check_output('ls')
        if ".rar" in q:
             print "Rar exists"
except subprocess.CalledProcessError as e:
        print e.output
