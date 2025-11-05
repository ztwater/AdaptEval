def baskets_from(items, maxbaskets=25):
    baskets = [[] for _ in range(maxbaskets)]
    for i, item in enumerate(items):
        baskets[i % maxbaskets].append(item)
    return filter(None, baskets) 
