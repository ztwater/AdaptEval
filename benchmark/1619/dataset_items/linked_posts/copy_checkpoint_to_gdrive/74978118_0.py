import tarfile


fd_path="/some/folder/path/"
fl_name="some_file_name.ext"
targz_fd_path_n_fl_name="/some/folder/path/some_file_name.tar.gz"

with tarfile.open(targz_fd_path_n_fl_name, "w:gz") as tar:
    tar.add(fd_path + fl_name, fl_name)
