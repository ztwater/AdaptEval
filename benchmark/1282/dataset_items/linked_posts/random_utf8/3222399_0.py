import itertools as it, operator as op

def max3bytes(unicode_string):

    # sequence of pairs of (char_in_string, u'\N{REPLACEMENT CHARACTER}')
    pairs= it.izip(unicode_string, it.repeat(u'\ufffd'))

    # is the argument less than or equal to 65535?
    selector= ft.partial(op.le, 65535)

    # using the character ordinals, return 0 or 1 based on `selector`
    indexer= it.imap(selector, it.imap(ord, unicode_string))

    # now pick the correct item for all pairs
    return u''.join(it.imap(tuple.__getitem__, pairs, indexer))
