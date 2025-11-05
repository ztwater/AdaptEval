def iter_baskets_contiguous(items, maxbaskets=3, item_count=None):
    '''
    generates balanced baskets from iterable, contiguous contents
    provide item_count if providing a iterator that doesn't support len()
    '''
    item_count = item_count or len(items)
    baskets = min(item_count, maxbaskets)
    items = iter(items)
    floor = item_count // baskets 
    ceiling = floor + 1
    stepdown = item_count % baskets
    for x_i in range(baskets):
        length = ceiling if x_i < stepdown else floor
        yield [items.next() for _ in range(length)]
