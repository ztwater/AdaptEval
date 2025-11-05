from pathlib import Path
path = Path("/my/directory/filename.txt")
try:
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
except OSError:
    # handle error; you can also catch specific errors like
    # FileExistsError and so on.
