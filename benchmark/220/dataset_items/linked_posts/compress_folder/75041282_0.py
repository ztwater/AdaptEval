import zipfile
from pathlib import Path
with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for path in Path("include_all_of_this_folder").rglob("*"):
        zf.write(path, path.as_posix())
