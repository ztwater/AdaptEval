>>> seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

>>> longest_subsequence(seq)
[0, 2, 6, 9, 11, 15]

>>> longest_subsequence(seq, order='decreasing')
[12, 10, 9, 5, 3]

>>> txt = ("Given an input sequence, what is the best way to find the longest"
               " (not necessarily continuous) non-decreasing subsequence.")

>>> ''.join(longest_subsequence(txt))
' ,abdegilnorsu'

>>> ''.join(longest_subsequence(txt, 'weak'))
'              ceilnnnnrsssu'

>>> ''.join(longest_subsequence(txt, 'weakly', 'decreasing'))
'vuutttttttssronnnnngeee.'

>>> dates = [
...   ('2015-02-03', 'name1'),
...   ('2015-02-04', 'nameg'),
...   ('2015-02-04', 'name5'),
...   ('2015-02-05', 'nameh'),
...   ('1929-03-12', 'name4'),
...   ('2023-07-01', 'name7'),
...   ('2015-02-07', 'name0'),
...   ('2015-02-08', 'nameh'),
...   ('2015-02-15', 'namex'),
...   ('2015-02-09', 'namew'),
...   ('1980-12-23', 'name2'),
...   ('2015-02-12', 'namen'),
...   ('2015-02-13', 'named'),
... ]

>>> longest_subsequence(dates, 'weak')

[('2015-02-03', 'name1'),
 ('2015-02-04', 'name5'),
 ('2015-02-05', 'nameh'),
 ('2015-02-07', 'name0'),
 ('2015-02-08', 'nameh'),
 ('2015-02-09', 'namew'),
 ('2015-02-12', 'namen'),
 ('2015-02-13', 'named')]

>>> from operator import itemgetter

>>> longest_subsequence(dates, 'weak', key=itemgetter(0))

[('2015-02-03', 'name1'),
 ('2015-02-04', 'nameg'),
 ('2015-02-04', 'name5'),
 ('2015-02-05', 'nameh'),
 ('2015-02-07', 'name0'),
 ('2015-02-08', 'nameh'),
 ('2015-02-09', 'namew'),
 ('2015-02-12', 'namen'),
 ('2015-02-13', 'named')]

>>> indices = set(longest_subsequence(dates, key=itemgetter(0), index=True))

>>> [e for i,e in enumerate(dates) if i not in indices]

[('2015-02-04', 'nameg'),
 ('1929-03-12', 'name4'),
 ('2023-07-01', 'name7'),
 ('2015-02-15', 'namex'),
 ('1980-12-23', 'name2')]
