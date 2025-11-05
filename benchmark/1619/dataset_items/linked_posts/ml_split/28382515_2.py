# symlink support under windows:
import os
os_symlink = getattr(os, "symlink", None)
if callable(os_symlink):
    pass
else:
    def symlink_ms(source, link_name):
        os.system("mklink {link} {target}".format(
            link = link_name,
            target = source.replace('/', '\\')))
    os.symlink = symlink_ms
