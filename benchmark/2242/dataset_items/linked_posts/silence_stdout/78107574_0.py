with contextlib.redirect_stdout(f := open(os.devnull, 'w')):
    ... # code continues
    f.close()
