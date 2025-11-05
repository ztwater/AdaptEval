>>> from simple_file_checksum import get_checksum
>>> get_checksum("path/to/file.txt")
'9e107d9d372bb6826bd81d3542a419d6'
>>> get_checksum("path/to/file.txt", algorithm="MD5")
'9e107d9d372bb6826bd81d3542a419d6'
