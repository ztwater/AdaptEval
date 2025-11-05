from typing import List, TypeVar

T = TypeVar('T')

def list_split(l: List[T], n: int) -> List[List[T]]:
    """split list into n chunks"""
    # ref: https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    k, m = divmod(len(l), n)
    return [l[i*k+min(i, m): (i+1)*k+min(i+1, m)] for i in range(n)]
    
