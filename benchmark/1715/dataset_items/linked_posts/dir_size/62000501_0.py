import os
def get_size(path = os.getcwd()):
    print("Calculating Size: ",path)
    total_size = 0
    #if path is directory--
    if os.path.isdir(path):
      print("Path type : Directory/Folder")
      for dirpath, dirnames, filenames in os.walk(path):
          for f in filenames:
              fp = os.path.join(dirpath, f)
              # skip if it is symbolic link
              if not os.path.islink(fp):
                  total_size += os.path.getsize(fp)
    #if path is a file---
    elif os.path.isfile(path):
      print("Path type : File")
      total_size=os.path.getsize(path)
    else:
      print("Path Type : Special File (Socket, FIFO, Device File)" )
      total_size=0
    bytesize=total_size
    print(bytesize, 'bytes')
    print(bytesize/(1024), 'kilobytes')
    print(bytesize/(1024*1024), 'megabytes')
    print(bytesize/(1024*1024*1024), 'gegabytes')
    return total_size


x=get_size("/content/examples")
