#!/usr/bin/python


first_names = ['Steve', 'Jane', 'Sara', 'Mary','Jack','Bob', 'Bily', 'Boni', 'Chris','Sori', 'Will', 'Won','Li']

def chunks(l, n):
for i in range(0, len(l), n):
    # Create an index range for l of n items:
    yield l[i:i+n]

result = list(chunks(first_names, 5))
print result
