import re

def natural_sort_key(s, _re=re.compile(r'(\d+)')):
    return [int(t) if i & 1 else t.lower() for i, t in enumerate(_re.split(s))]

...
my_naturally_sorted_list = sorted(my_list, key=natural_sort_key)
