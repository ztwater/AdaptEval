for dirname in os.listdir(rootdir):
  if os.path.isdir(os.path.join(rootdir, dirname)):
     print("I got a subdirectory: %s" % dirname)
