from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

def make_zip(tree_path, zip_path, mode='w', skip_empty_dir=False):
    with ZipFile(zip_path, mode=mode, compression=ZIP_DEFLATED) as zf:
        paths = [Path(tree_path)]
        while paths:
            p = paths.pop()
            if p.is_dir():
                paths.extend(p.iterdir())
                if skip_empty_dir:
                    continue
            zf.write(p)
