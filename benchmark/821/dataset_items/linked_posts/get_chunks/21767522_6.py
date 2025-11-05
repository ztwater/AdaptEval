from itertools import cycle
from typing import List, Any

def cycle_baskets(items: List[Any], maxbaskets: int) -> List[List[Any]]:
    baskets = [[] for _ in range(min(maxbaskets, len(items)))]
    for item, basket in zip(items, cycle(baskets)):
        basket.append(item)
    return baskets
