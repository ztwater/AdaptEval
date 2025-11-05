def report(blocknr, blocksize, size):
    current = blocknr*blocksize
    sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))

def downloadFile(url):
    print "\n",url
    fname = url.split('/')[-1]
    print fname
    urllib.urlretrieve(url, fname, report)
