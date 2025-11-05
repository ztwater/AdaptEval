def CREATEZIPFILE(zipname, path):
    #function to create a zip file
    #Parameters: zipname - name of the zip file; path - name of folder/file to be put in zip file

    zipf = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    zipf.setpassword(b"password") #if you want to set password to zipfile

    #checks if the path is file or directory
    if os.path.isdir(path):
        for files in os.listdir(path):
            zipf.write(os.path.join(path, files), files)

    elif os.path.isfile(path):
        zipf.write(os.path.join(path), path)
    zipf.close()
