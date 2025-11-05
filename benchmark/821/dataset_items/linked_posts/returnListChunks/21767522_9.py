from itertools import islice
from typing import List, Any, Generator
    
def yield_islice_baskets(items: List[Any], maxbaskets: int) -> Generator[List[Any], None, None]:
    n_baskets = min(maxbaskets, len(items))
    for i in range(n_baskets):
        yield islice(items, i, None, n_baskets)
