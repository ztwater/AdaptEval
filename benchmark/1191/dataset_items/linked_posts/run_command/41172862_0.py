import subprocess

# To redirect stdout (only):
subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.DEVNULL
)

# to redirect stderr to /dev/null as well:
subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.DEVNULL
)

# Alternatively, you can merge stderr and stdout streams and redirect
# the one stream to /dev/null
subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.STDOUT
)
