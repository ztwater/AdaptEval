with stdchannel_redirected(sys.stderr, os.devnull):
    if compiler.has_function('clock_gettime', libraries=['rt']):
        libraries.append('rt')
