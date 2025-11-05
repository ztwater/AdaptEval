def txt2filename(txt, chr_set='normal'):
    """Converts txt to a valid Windows/*nix filename with printable characters only.

    args:
        txt: The str to convert.
        chr_set: 'normal', 'universal', or 'inclusive'.
            'universal':    ' -.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            'normal':       Every printable character exept those disallowed on Windows/*nix.
            'extended':     All 'normal' characters plus the extended character ASCII codes 128-255
    """

    FILLER = '-'

    # Step 1: Remove excluded characters.
    if chr_set == 'universal':
        # Lookups in a set are O(n) vs O(n * x) for a str.
        printables = set(' -.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    else:
        if chr_set == 'normal':
            max_chr = 127
        elif chr_set == 'extended':
            max_chr = 256
        else:
            raise ValueError(f'The chr_set argument may be normal, extended or universal; not {chr_set=}')
        EXCLUDED_CHRS = set(r'<>:"/\|?*')               # Illegal characters in Windows filenames.
        EXCLUDED_CHRS.update(chr(127))                  # DEL (non-printable).
        printables = set(chr(x)
                         for x in range(32, max_chr)
                         if chr(x) not in EXCLUDED_CHRS)
    result = ''.join(x if x in printables else FILLER   # Allow printable characters only.
                     for x in txt)

    # Step 2: Device names, '.', and '..' are invalid filenames in Windows.
    DEVICE_NAMES = 'CON,PRN,AUX,NUL,COM1,COM2,COM3,COM4,' \
                   'COM5,COM6,COM7,COM8,COM9,LPT1,LPT2,' \
                   'LPT3,LPT4,LPT5,LPT6,LPT7,LPT8,LPT9,' \
                   'CONIN$,CONOUT$,..,.'.split()        # This list is an O(n) operation.
    if result in DEVICE_NAMES:
        result = f'-{result}-'

    # Step 3: Maximum length of filename is 255 bytes in Windows and Linux (other *nix flavors may allow longer names).
    result = result[:255]

    # Step 4: Windows does not allow filenames to end with '.' or ' ' or begin with ' '.
    result = re.sub(r'^[. ]', FILLER, result)
    result = re.sub(r' $', FILLER, result)

    return result
