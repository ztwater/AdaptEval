import subprocess
import sys

def install(name):
    subprocess.call([sys.executable, '-m', 'pip', 'install', name])
