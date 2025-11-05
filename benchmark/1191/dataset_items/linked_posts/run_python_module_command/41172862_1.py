import os
import subprocess

with open(os.devnull, 'w') as devnull:
    subprocess.run(
        ['ls', '-l'],
        stdout = devnull
    )
