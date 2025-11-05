import gconf
conf = gconf.client_get_default()
conf.set_string('/desktop/gnome/background/picture_filename','/path/to/filename.jpg')
