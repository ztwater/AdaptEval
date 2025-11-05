import subprocess

result = subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.PIPE,
    universal_newlines = True # Python >= 3.7 also accepts "text=True"
)
print(result.stdout)

# To also capture stderr...
result = subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines = True # Python >= 3.7 also accepts "text=True"
)
print(result.stdout)
print(result.stderr)

# To mix stdout and stderr into a single string
result = subprocess.run(
    ['ls', '-l'],
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT,
    universal_newlines = True # Python >= 3.7 also accepts "text=True"
)
print(result.stdout)
