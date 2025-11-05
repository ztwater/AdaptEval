encoding = "utf-8" # or iso-8859-15, or cp1252, or whatever encoding you use
byte_string = b"café"  # or simply "café" before python 3.
unicode_string = byte_string.decode(encoding)
