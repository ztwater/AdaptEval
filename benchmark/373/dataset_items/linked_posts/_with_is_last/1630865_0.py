from itertools import tee, izip
items, between = tee(input_iterator, 2)  # Input must be an iterator.
first = items.next()
do_to_every_item(first)  # All "do to every" operations done to first item go here.
for i, b in izip(items, between):
    do_between_items(b)  # All "between" operations go here.
    do_to_every_item(i)  # All "do to every" operations go here.
