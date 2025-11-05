if not 'SUDO_UID' in os.environ:
    print "this program requires super user priv."
    sys.exit(1)
