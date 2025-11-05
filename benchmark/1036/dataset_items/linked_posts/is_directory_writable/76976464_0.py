def isWritable(path: str) -> bool:
    try:
        filename  = os.path.join(path, 'write_test.txt')
        f = open(filename,"w")
        f.close()
        os.remove(filename)
        return True
    except:
        return False
