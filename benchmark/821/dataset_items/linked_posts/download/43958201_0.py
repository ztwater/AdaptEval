import sys
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False


def progress_callback_simple(downloaded,total):
    sys.stdout.write(
        "\r" +
        (len(str(total))-len(str(downloaded)))*" " + str(downloaded) + "/%d"%total +
        " [%3.2f%%]"%(100.0*float(downloaded)/float(total))
    )
    sys.stdout.flush()

def download(srcurl, dstfilepath, progress_callback=None, block_size=8192):
    def _download_helper(response, out_file, file_size):
        if progress_callback!=None: progress_callback(0,file_size)
        if block_size == None:
            buffer = response.read()
            out_file.write(buffer)

            if progress_callback!=None: progress_callback(file_size,file_size)
        else:
            file_size_dl = 0
            while True:
                buffer = response.read(block_size)
                if not buffer: break

                file_size_dl += len(buffer)
                out_file.write(buffer)

                if progress_callback!=None: progress_callback(file_size_dl,file_size)
    with open(dstfilepath,"wb") as out_file:
        if python3:
            with urllib.request.urlopen(srcurl) as response:
                file_size = int(response.getheader("Content-Length"))
                _download_helper(response,out_file,file_size)
        else:
            response = urllib2.urlopen(srcurl)
            meta = response.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            _download_helper(response,out_file,file_size)

import traceback
try:
    download(
        "https://geometrian.com/data/programming/projects/glLib/glLib%20Reloaded%200.5.9/0.5.9.zip",
        "output.zip",
        progress_callback_simple
    )
except:
    traceback.print_exc()
    input()
