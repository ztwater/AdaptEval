name = ['Megan', 'Harriet', 'Henry', 'Beth', 'George']

score_list = [9, 6, 5, 6, 10]
d = dict(zip(name, score_list))

from operator import itemgetter
print(sorted(d.items(), key=itemgetter(0)))
[('Beth', 6), ('George', 10), ('Harriet', 6), ('Henry', 5), ('Megan', 9)]
