import tarfile
import os.path

source_location = r'C:\Users\username\Desktop\New folder'
output_name = r'C:\Users\username\Desktop\new.tar.gz'

# ---------------------------------------------------
#  --- output new.tar.gz with 'New folder' inside ---
#  -> new.tar.gz/New folder/aaaa/a.txt 
#  -> new.tar.gz/New folder/bbbb/b.txt
# ---------------------------------------------------
# def make_tarfile(output_filename, source_dir):
#     with tarfile.open(output_filename, "w:gz") as tar:
#         # tar.add(source_dir, arcname=os.path.basename(source_dir))
#         tar.add(source_dir, arcname=os.path.sep(source_dir))


# ---------------------------------------------------
#  --- output new.tar.gz without 'New folder' inside ---
#  -> new.tar.gz/aaaa/a.txt 
#  -> new.tar.gz/bbbb/b.txt
# ---------------------------------------------------
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                tar.add(file_path, arcname=arcname)

try:
    make_tarfile(output_name, source_location)

except Exception as e:
    print(f"Error: {e}")
