import hashlib
with open(path, "rb") as f:
    digest = hashlib.file_digest(f, "md5")
print(digest.hexdigest())
