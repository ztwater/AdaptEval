from pathlib import Path
import zipfile

fp_zip = Path("output.zip")
path_to_archive = Path("./path-to-archive")

with zipfile.ZipFile(fp_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for fp in path_to_archive.glob("**/*"):
        zipf.write(fp, arcname=fp.relative_to(path_to_archive))
