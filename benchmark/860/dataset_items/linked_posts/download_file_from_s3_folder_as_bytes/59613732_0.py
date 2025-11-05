...
tmp = tempfile.NamedTemporaryFile()

with open(tmp.name, 'wb') as f:
    object.download_fileobj(f)
    f.seek(0,2) 
    img=mpimg.imread(tmp.name)
    print (img.shape)

