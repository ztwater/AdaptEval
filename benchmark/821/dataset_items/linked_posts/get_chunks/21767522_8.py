from typing import List, Any

def slice_baskets(items: List[Any], maxbaskets: int) -> List[List[Any]]:
    n_baskets = min(maxbaskets, len(items))
    return [items[i::n_baskets] for i in range(n_baskets)]
