with zipfile.ZipFile("listdir.zip", "w" ) as myzip:
    for f in os.listdir():
        if f == "listdir.zip":
            # Creating a listdir.zip in the same directory
            # will include listdir.zip inside itself, beware of this
            continue
        zipall(myzip, f)
