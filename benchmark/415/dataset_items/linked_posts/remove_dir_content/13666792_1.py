import os
import shutil

# Gather directory contents
contents = [os.path.join(target_dir, i) for i in os.listdir(target_dir)]

# Iterate and remove each item in the appropriate manner
[shutil.rmtree(i) if os.path.isdir(i) and not os.path.islink(i) else os.remove(i) for i in contents]
