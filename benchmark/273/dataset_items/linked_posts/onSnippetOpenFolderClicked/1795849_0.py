if sys.platform=='win32':
    subprocess.Popen(['start', d], shell= True)

elif sys.platform=='darwin':
    subprocess.Popen(['open', d])

else:
    try:
        subprocess.Popen(['xdg-open', d])
    except OSError:
        # er, think of something else to try
        # xdg-open *should* be supported by recent Gnome, KDE, Xfce
