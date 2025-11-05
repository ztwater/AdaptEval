import fs

home_fs = fs.open_fs("~")
home_fs.opendir("/Videos").removetree("/")
home_fs.exists("/Videos")  # True
home_fs.isempty("/Videos")  # True
