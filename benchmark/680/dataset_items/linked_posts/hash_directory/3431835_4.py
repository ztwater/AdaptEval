[(fname, hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.sha256()))
    for fname in fnamelst]
