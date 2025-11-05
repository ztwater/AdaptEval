In [6]: get_size('/etc/not-exist-path')
Out[6]: 0
In [7]: get_size('.')
Out[7]: 12038689
In [8]: def filesize(size: int) -> str:
   ...:     for unit in ("B", "K", "M", "G", "T"):
   ...:         if size < 1024:
   ...:             break
   ...:         size /= 1024
   ...:     return f"{size:.1f}{unit}"
   ...:

In [9]: filesize(get_size('.'))
Out[9]: '11.5M'

