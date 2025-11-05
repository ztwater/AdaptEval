>>> file_uri_to_path("file:///etc/hosts")
PurePosixPath('/etc/hosts')

>>> file_uri_to_path("file:///etc/hosts", pathlib.PurePosixPath)
PurePosixPath('/etc/hosts')

>>> file_uri_to_path("file:///C:/Program Files/Steam/", pathlib.PureWindowsPath)
PureWindowsPath('C:/Program Files/Steam')

>>> file_uri_to_path("file:/proc/cpuinfo", pathlib.PurePosixPath)
PurePosixPath('/proc/cpuinfo')

>>> file_uri_to_path("file:c:/system32/etc/hosts", pathlib.PureWindowsPath)
PureWindowsPath('c:/system32/etc/hosts')
