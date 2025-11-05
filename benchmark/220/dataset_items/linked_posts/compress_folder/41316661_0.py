import os
import zipfile

def zip_dir(path_dir, path_file_zip=''):
if not path_file_zip:
    path_file_zip = os.path.join(
        os.path.dirname(path_dir), os.path.basename(path_dir)+'.zip')
with zipfile.ZipFile(path_file_zip, 'wb', zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(path_dir):
        for file_or_dir in files + dirs:
            zip_file.write(
                os.path.join(root, file_or_dir),
                os.path.relpath(os.path.join(root, file_or_dir),
                                os.path.join(path_dir, os.path.pardir)))
