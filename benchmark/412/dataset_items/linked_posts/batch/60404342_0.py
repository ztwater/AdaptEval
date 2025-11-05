def batch(items: Iterable, batch_size: int) -> Iterable[Iterable]:
    # enumerate items and group them by batch index
    enumerated_item_groups = itertools.groupby(enumerate(items), lambda t: t[0] // batch_size)
    # extract items from enumeration tuples
    item_batches = ((t[1] for t in enumerated_items) for key, enumerated_items in enumerated_item_groups)
    return item_batches
