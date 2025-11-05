[(fname, hashlib.sha256(file_as_bytes(open(fname, 'rb'))).digest()) for fname in fnamelst]
