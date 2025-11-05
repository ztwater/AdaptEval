>>> import natsort
>>> your_list = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])
>>> print ',\n'.join(natsort.natsorted(your_list))
4 sheets,
12 sheets,
48 sheets,
booklet
