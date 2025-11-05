import os, shutil
var_0 = '/path/to/folder'
for filename in os.listdir(var_0):
    var_1 = os.path.join(var_0, filename)
    try:
        if os.path.isfile(var_1) or os.path.islink(var_1):
            os.unlink(var_1)
        elif os.path.isdir(var_1):
            shutil.rmtree(var_1)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (var_1, e))
