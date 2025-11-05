import tarfile
import os

fd_path_n_fl_name="/some/folder/path/some_file_name.ext"
targz_fd_path_n_fl_name="/some/folder/path/some_file_name.tar.gz"

with tarfile.open(targz_fd_path_n_fl_name, "w:gz") as tar:
    tar.add(fd_path_n_fl_name, os.path.basename(fd_path_n_fl_name))
