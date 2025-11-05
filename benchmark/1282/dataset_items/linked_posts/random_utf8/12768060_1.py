def filter_4byte_chars(s):
    i = 0
    j = len(s)
    # you need to convert
    # the immutable string
    # to a mutable list first
    s = list(s)
    while i < j:
        # get the value of this byte
        k = ord(s[i])
        # this is a 1-byte character, skip to the next byte
        if k <= 127:
            i += 1
        # this is a 2-byte character, skip ahead by 2 bytes
        elif k < 224:
            i += 2
        # this is a 3-byte character, skip ahead by 3 bytes
        elif k < 240:
            i += 3
        # this is a 4-byte character, remove it and update
        # the length of the string we need to check
        else:
            s[i:i+4] = []
            j -= 4
    return ''.join(s)
