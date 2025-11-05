>>> d = ddict()
>>> d[1]['a'][True] = 0.5
>>> d[1]['b'] = 3
>>> import pprint; pprint.pprint(d)
defaultdict(<function ddict at 0x7fcac68bf048>,
            {1: defaultdict(<function ddict at 0x7fcac68bf048>,
                            {'a': defaultdict(<function ddict at 0x7fcac68bf048>,
                                              {True: 0.5}),
                             'b': 3})})
