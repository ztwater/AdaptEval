a = '&#'

to_replace = ['&', '#']

for char in to_replace:
    a = a.replace(char, "\\"+char)

print(a)

>>> \&\#
