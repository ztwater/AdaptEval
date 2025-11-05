input_list [1, 1, 1, 1, 1, 1, 1]

import operator

def all_items_in_list_are_equal(l: list) -> bool:

    all_items_are_equal = \
        all(
            map(
                operator.eq,
                l[1:],
                l[:-1]
            )
        )

    return all_items_are_equal
