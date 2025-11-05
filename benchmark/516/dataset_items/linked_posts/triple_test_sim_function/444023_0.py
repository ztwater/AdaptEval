>>> os.path.exists('/tmp/dirname')
True
>>> os.path.exists('/tmp/dirname/filename.etc')
True
>>> os.path.isdir('/tmp/dirname/filename.etc')
False
>>> os.path.isdir('/tmp/fakedirname')
False
