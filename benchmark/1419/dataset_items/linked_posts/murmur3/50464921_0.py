def bytes_to_long(bytes):
    length = len(bytes)
    if length < 8:
        extra = 8 - length
        bytes = b'\000' * extra + bytes
    assert len(bytes) == 8
   return sum((b << (k * 8) for k, b in enumerate(bytes)))
