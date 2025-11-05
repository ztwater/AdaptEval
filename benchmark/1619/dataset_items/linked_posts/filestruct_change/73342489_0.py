os_symlink = getattr(os, "symlink", None)
if callable(os_symlink):
    pass
else:
    print "Patching windows symlink support"
    def symlink_ms(source, link_name):
        import ctypes
        import ctypes.wintypes as wintypes
        if os.path.exists(link_name):
            df = ctypes.windll.kernel32.DeleteFileW
            if df(link_name) == 0:
                print "Could not remove existing file:", link_name
                print "You should remove the file manually through Explorer or an elevated cmd process."
                raise ctypes.WinError()
        csl = ctypes.windll.kernel32.CreateSymbolicLinkW
        csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
        csl.restype = ctypes.c_ubyte
        flags = 1 if os.path.isdir(source) else 0
        flags += 2 # For unprivileged mode. Requires Developer Mode to be activated.
        if csl(link_name, source, flags) == 0:
            raise ctypes.WinError()
    os.symlink = symlink_ms
