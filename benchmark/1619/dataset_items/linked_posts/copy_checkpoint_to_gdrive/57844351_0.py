import tarfile

with tarfile.open("save.tar.gz","w:gz") as tar:
      for file in ["a.txt","b.log","c.png"]:
           tar.add(os.path.basename(file))
