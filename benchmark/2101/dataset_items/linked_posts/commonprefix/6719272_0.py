import itertools

strings = ['my_prefix_what_ever', 
           'my_prefix_what_so_ever', 
           'my_prefix_doesnt_matter']

def all_same(x):
    return all(x[0] == y for y in x)

char_tuples = itertools.izip(*strings)
prefix_tuples = itertools.takewhile(all_same, char_tuples)
''.join(x[0] for x in prefix_tuples)
