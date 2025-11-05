input_list [1, 1, 1, 1, 1, 1, 1]

import operator
from itertools import pairwise
from itertools import starmap

def all_items_in_list_are_equal(l: list) -> bool:

    all_items_are_equal = \
        all(
            starmap(
                operator.eq,
                pairwise(l)
            )
        )

    return all_items_are_equal
