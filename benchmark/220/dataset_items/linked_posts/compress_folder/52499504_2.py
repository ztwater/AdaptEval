cwd = os.getcwd()
files = [os.path.join(cwd, f) for f in ['dir4', 'root.txt']]

with zipfile.ZipFile("selective.zip", "w" ) as myzip:
    for f in files:
        zipall(myzip, f)
