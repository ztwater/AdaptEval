from __future__ import print_function
import os
import sys
import operator

def null_decorator(ob):
    return ob

if sys.version_info >= (3,2,0):
    import functools
    my_cache_decorator = functools.lru_cache(maxsize=4096)
else:
    my_cache_decorator = null_decorator

start_dir = os.path.normpath(os.path.abspath(sys.argv[1])) if len(sys.argv) > 1 else '.'

@my_cache_decorator
def get_dir_size(start_path = '.'):
    total_size = 0
    if 'scandir' in dir(os):
        # using fast 'os.scandir' method (new in version 3.5)
        for entry in os.scandir(start_path):
            if entry.is_dir(follow_symlinks = False):
                total_size += get_dir_size(entry.path)
            elif entry.is_file(follow_symlinks = False):
                total_size += entry.stat().st_size
    else:
        # using slow, but compatible 'os.listdir' method
        for entry in os.listdir(start_path):
            full_path = os.path.abspath(os.path.join(start_path, entry))
            if os.path.isdir(full_path):
                total_size += get_dir_size(full_path)
            elif os.path.isfile(full_path):
                total_size += os.path.getsize(full_path)
    return total_size

def get_dir_size_walk(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def bytes2human(n, format='%(value).0f%(symbol)s', symbols='customary'):
    """
    (c) http://code.activestate.com/recipes/578019/

    Convert n bytes into a human readable string based on format.
    symbols can be either "customary", "customary_ext", "iec" or "iec_ext",
    see: http://goo.gl/kTQMs

      >>> bytes2human(0)
      '0.0 B'
      >>> bytes2human(0.9)
      '0.0 B'
      >>> bytes2human(1)
      '1.0 B'
      >>> bytes2human(1.9)
      '1.0 B'
      >>> bytes2human(1024)
      '1.0 K'
      >>> bytes2human(1048576)
      '1.0 M'
      >>> bytes2human(1099511627776127398123789121)
      '909.5 Y'

      >>> bytes2human(9856, symbols="customary")
      '9.6 K'
      >>> bytes2human(9856, symbols="customary_ext")
      '9.6 kilo'
      >>> bytes2human(9856, symbols="iec")
      '9.6 Ki'
      >>> bytes2human(9856, symbols="iec_ext")
      '9.6 kibi'

      >>> bytes2human(10000, "%(value).1f %(symbol)s/sec")
      '9.8 K/sec'

      >>> # precision can be adjusted by playing with %f operator
      >>> bytes2human(10000, format="%(value).5f %(symbol)s")
      '9.76562 K'
    """
    SYMBOLS = {
        'customary'     : ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'),
        'customary_ext' : ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
                           'zetta', 'iotta'),
        'iec'           : ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
        'iec_ext'       : ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
                           'zebi', 'yobi'),
    }
    n = int(n)
    if n < 0:
        raise ValueError("n < 0")
    symbols = SYMBOLS[symbols]
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i+1)*10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)

############################################################
###
###  main ()
###
############################################################
if __name__ == '__main__':
    dir_tree = {}
    ### version, that uses 'slow' [os.walk method]
    #get_size = get_dir_size_walk
    ### this recursive version can benefit from caching the function calls (functools.lru_cache)
    get_size = get_dir_size

    for root, dirs, files in os.walk(start_dir):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if os.path.isdir(dir_path):
                dir_tree[dir_path] = get_size(dir_path)

    for d, size in sorted(dir_tree.items(), key=operator.itemgetter(1), reverse=True):
        print('%s\t%s' %(bytes2human(size, format='%(value).2f%(symbol)s'), d))

    print('-' * 80)
    if sys.version_info >= (3,2,0):
        print(get_dir_size.cache_info())
