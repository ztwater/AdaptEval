import glob
import shutil
dest_dir = "C:/test"
for file in glob.glob(r'C:/*.txt'):
    print(file)
    shutil.copy(file, dest_dir)
