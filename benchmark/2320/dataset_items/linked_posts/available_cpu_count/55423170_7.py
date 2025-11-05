import psutil
print(len(psutil.Process().cpu_affinity()))
