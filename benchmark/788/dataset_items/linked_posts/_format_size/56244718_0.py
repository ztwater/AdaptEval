from pathlib import Path    

def get_size(path = Path('.')):
    """ Gets file size, or total directory size """
    if path.is_file():
        size = path.stat().st_size
    elif path.is_dir():
        size = sum(file.stat().st_size for file in path.glob('*.*'))
    return size

def format_size(path, unit="MB"):
    """ Converts integers to common size units used in computing """
    bit_shift = {"B": 0,
            "kb": 7,
            "KB": 10,
            "mb": 17,
            "MB": 20,
            "gb": 27,
            "GB": 30,
            "TB": 40,}
    return "{:,.0f}".format(get_size(path) / float(1 << bit_shift[unit])) + " " + unit

# Tests and test results
>>> get_size("d:\\media\\bags of fun.avi")
'38 MB'
>>> get_size("d:\\media\\bags of fun.avi","KB")
'38,763 KB'
>>> get_size("d:\\media\\bags of fun.avi","kb")
'310,104 kb'
