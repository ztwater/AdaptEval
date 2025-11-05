import tarfile
tar = tarfile.open("sample.tar.gz", "w:gz")
for name in ["file1", "file2", "file3"]:
    tar.add(name)
tar.close()
