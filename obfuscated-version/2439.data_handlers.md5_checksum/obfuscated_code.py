import hashlib
def md5(var_0):
    var_1 = hashlib.md5()
    with open(var_0, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            var_1.update(chunk)
    return var_1.hexdigest()
