first = True
for element in iterable:
    if first:
        do_extra_thing(element)
        first = False
    do_normal_thing(element)
