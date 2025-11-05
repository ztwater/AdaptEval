def kbin(l, k, ordered=True):
    """
    Return sequence ``l`` partitioned into ``k`` bins.

    Examples
    ========

    The default is to give the items in the same order, but grouped
    into k partitions:

    >>> for p in kbin(range(5), 2):
    ...     print p
    ...
    [[0], [1, 2, 3, 4]]
    [[0, 1], [2, 3, 4]]
    [[0, 1, 2], [3, 4]]
    [[0, 1, 2, 3], [4]]

    Setting ``ordered`` to None means that the order of the elements in
    the bins is irrelevant and the order of the bins is irrelevant. Though
    they are returned in a canonical order as lists of lists, all lists
    can be thought of as sets.

    >>> for p in kbin(range(3), 2, ordered=None):
    ...     print p
    ...
    [[0, 1], [2]]
    [[0], [1, 2]]
    [[0, 2], [1]]

    """
    from sympy.utilities.iterables import (
        permutations, multiset_partitions, partitions)

    def partition(lista, bins):
        #  EnricoGiampieri's partition generator from
        #  http://stackoverflow.com/questions/13131491/
        #  partition-n-items-into-k-bins-in-python-lazily
        if len(lista) == 1 or bins == 1:
            yield [lista]
        elif len(lista) > 1 and bins > 1:
            for i in range(1, len(lista)):
                for part in partition(lista[i:], bins - 1):
                    if len([lista[:i]] + part) == bins:
                        yield [lista[:i]] + part
    if ordered:
        for p in partition(l, k):
            yield p
    else:
        for p in multiset_partitions(l, k):
            yield p
