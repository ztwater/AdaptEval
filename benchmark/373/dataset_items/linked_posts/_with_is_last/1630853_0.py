def item_processing( item ):
    # *the common processing*

head_tail_iter = iter( someSequence )
head = next(head_tail_iter)
item_processing( head )
for item in head_tail_iter:
    # *the between processing*
    item_processing( item )
