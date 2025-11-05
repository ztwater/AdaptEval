p1 = subprocess.Popen('ls ...', stdout=subprocess.PIPE)
p2 = subprocess.Popen('sed ...', stdin=p1.stdout, stdout=subprocess.PIPE)
print p2.communicate()
