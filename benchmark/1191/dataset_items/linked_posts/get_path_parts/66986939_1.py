def split_path_iter(string, lst):
    head, tail = os_path.split(string)
    if head == '':
        return [string] + lst
    else:
        return split_path_iter(head, [tail] + lst)

def split_path(string):
    return split_path_iter(string, [])
