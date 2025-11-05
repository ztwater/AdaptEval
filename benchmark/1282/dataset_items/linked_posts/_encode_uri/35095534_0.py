from cytoolz.functoolz import compose
from cytoolz.itertoolz import chain,sliding_window
from itertools import starmap,imap,ifilter
from operator import itemgetter,contains
text='&hello#hi&yo&'
char_index_iter=compose(partial(imap, itemgetter(0)), partial(ifilter, compose(partial(contains, '#&'), itemgetter(1))), enumerate)
print '\\'.join(imap(text.__getitem__, starmap(slice, sliding_window(2, chain((0,), char_index_iter(text), (len(text),))))))
