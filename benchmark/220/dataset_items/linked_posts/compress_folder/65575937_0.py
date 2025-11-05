import zipfile
from pathlib import Path

def zip_dir(path: Path, zip_file_path: Path):
    """Zip all contents of path to zip_file"""
    files_to_zip = [
        file for file in path.glob('*') if file.is_file()]
    with zipfile.ZipFile(
        zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_f:
        for file in files_to_zip:
            print(file.name)
            zip_f.write(file, file.name)

current_dir = Path.cwd()  
tozip_dir = current_dir / "test"
zip_dir(
    tozip_dir, current_dir / 'dir.zip')
