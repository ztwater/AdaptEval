>>> humanize.naturalsize(1000000)
'1.0 MB'
>>> humanize.naturalsize(1000000, binary=True)
'976.6 KiB'
>>> humanize.naturalsize(1000000, gnu=True)
'976.6K'
