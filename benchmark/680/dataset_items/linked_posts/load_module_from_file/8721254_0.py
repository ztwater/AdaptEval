path = os.path.join('./path/to/folder/with/py/files', '*.py')
for infile in glob.glob(path):
    basename = os.path.basename(infile)
    basename_without_extension = basename[:-3]

    # http://docs.python.org/library/imp.html?highlight=imp#module-imp
    imp.load_source(basename_without_extension, infile)
