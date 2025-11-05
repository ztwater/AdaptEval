import os

def du(directory):
    # add size of the top directory (special file)
    size=os.lstat(directory).st_size

    inodes_sizes={}
    for dirpath, dirnames, filenames in os.walk(directory):
        # add sizes of subdirectories (special files)
        for d in dirnames:            
            size+=os.lstat(os.path.join(dirpath, d)).st_size
        # get sizes for unique inodes (to include all hard links to a single file once)            
        for f in filenames:            
            file_stat=os.lstat(os.path.join(dirpath, f))
            inode=file_stat.st_ino
            inode_size=file_stat.st_size
            inodes_sizes[inode]=inode_size   

    # add sizes of files
    size+=sum(inodes_sizes.values())
    return(size)
