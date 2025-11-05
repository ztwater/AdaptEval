import os

def get_size(var_0 = '.'):
    var_1 = 0
    for dirpath, dirnames, filenames in os.walk(var_0):
        for f in filenames:
            var_2 = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(var_2):
                var_1 += os.path.getsize(var_2)

    return var_1
 