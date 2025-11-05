def iter_baskets_from(items, maxbaskets=3):
    '''generates evenly balanced baskets from indexable iterable'''
    item_count = len(items)
    baskets = min(item_count, maxbaskets)
    for x_i in range(baskets):
        yield [items[y_i] for y_i in range(x_i, item_count, baskets)]
    
