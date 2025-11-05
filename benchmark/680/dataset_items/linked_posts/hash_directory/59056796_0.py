import hashlib
with open("your_filename.txt", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.digest())
print(file_hash.hexdigest())  # to get a printable str instead of bytes
