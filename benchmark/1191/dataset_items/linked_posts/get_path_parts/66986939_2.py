def split_path(string):
    head, tail = os_path.split(string)
    if head == '':
        return [string]
    else:
        return split_path(head) + [tail]
