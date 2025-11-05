from pathlib import Path
from shutil import rmtree

for path in Path("/path/to/folder").glob("**/*"):
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        rmtree(path)
