# In test.py

from importmonkey import add_path
add_path("../relative/path")  # relative to current __file__
add_path("/my/absolute/path/to/somewhere")  # absolute path
import project

# You can add as many paths as needed, absolute or relative, in any file.
# Relative paths start from the current __file__ directory.
# Normal unix path conventions work so you can use '..' and '.' and so on.
# The paths you try to add are checked for validity etc. help(add_path) for details.

