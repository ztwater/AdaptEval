def batch_advanced(items: Iterable, batch_size: int, batches_mapper: Callable[[Iterable], Any] = None) -> Iterable[Iterable]:
    enumerated_item_groups = itertools.groupby(enumerate(items), lambda t: t[0] // batch_size)
    if batches_mapper:
        item_batches = (batches_mapper(t[1] for t in enumerated_items) for key, enumerated_items in enumerated_item_groups)
    else:
        item_batches = ((t[1] for t in enumerated_items) for key, enumerated_items in enumerated_item_groups)
    return item_batches
