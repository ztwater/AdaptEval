from math import log
def human_readable_bytes(x):
    # hybrid of https://stackoverflow.com/a/10171475/2595465
    #      with https://stackoverflow.com/a/5414105/2595465
    if x == 0: return '0'
    magnitude = int(log(abs(x),10.24))
    if magnitude > 16:
        format_str = '%iP'
        denominator_mag = 15
    else:
        float_fmt = '%2.1f' if magnitude % 3 == 1 else '%1.2f'
        illion = (magnitude + 1) // 3
        format_str = float_fmt + ['', 'K', 'M', 'G', 'T', 'P'][illion]
    return (format_str % (x * 1.0 / (1024 ** illion))).lstrip('0')
