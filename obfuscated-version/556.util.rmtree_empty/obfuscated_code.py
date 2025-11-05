import os


def delete_empty_folders(var_0):

    var_1 = set()
    
    for current_dir, subdirs, files in os.walk(var_0, topdown=False):

        var_2 = False
        for subdir in subdirs:
            if os.path.join(current_dir, subdir) not in var_1:
                var_2 = True
                break
    
        if not any(files) and not var_2:
            os.rmdir(current_dir)
            var_1.add(current_dir)

    return var_1

