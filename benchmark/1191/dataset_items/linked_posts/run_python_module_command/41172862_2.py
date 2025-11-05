import subprocess

result = subprocess.run(
    ['ls', '-l'],
    capture_output = True, # Python >= 3.7 only
    text = True # Python >= 3.7 only
)
print(result.stdout)
print(result.stderr)
