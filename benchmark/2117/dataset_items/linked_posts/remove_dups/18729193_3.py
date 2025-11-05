import operator
def unique(lst, cmp_op=operator.ne):
    return [] if lst==[] else [lst[0]] + unique(filter(lambda x: cmp_op(x, lst[0]), lst[1:]), cmp_op)
