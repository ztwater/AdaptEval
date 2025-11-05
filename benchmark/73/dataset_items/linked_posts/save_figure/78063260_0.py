from urllib.request import urlretrieve

if __name__ == '__main__':
    urlretrieve(url, filename, printProgress)
    print(end='\r')


def printProgress(blocknum, bs, size):
    percent = (blocknum * bs) / size
    done = "#" * int(40 * percent)
    print(f'\r[{done:<40}] {percent:.1%}', end='')
