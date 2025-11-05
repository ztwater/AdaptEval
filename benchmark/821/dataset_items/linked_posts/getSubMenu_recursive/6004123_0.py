>>> import subprocess
>>> subprocess.check_output(['mkdir', '-p', 'first/second/third']) 
# Equivalent to running 'mkdir -p first/second/third' in a shell (which creates
# parent directories if they do not yet exist).

>>> subprocess.check_output(['chown', '-R', 'dail:users', 'first'])
# Recursively change owner to 'dail' and group to 'users' for 'first' and all of
# its subdirectories.

>>> subprocess.check_output(['chmod', '-R', 'g+w', 'first'])
# Add group write permissions to 'first' and all of its subdirectories.
