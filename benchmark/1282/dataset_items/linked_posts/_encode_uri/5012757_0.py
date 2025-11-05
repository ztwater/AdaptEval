def mk_esc(esc_chars):
    return lambda s: ''.join(['\\' + c if c in esc_chars else c for c in s])

>>> esc = mk_esc('&#')
>>> print esc('Learn & be #1')
Learn \& be \#1
