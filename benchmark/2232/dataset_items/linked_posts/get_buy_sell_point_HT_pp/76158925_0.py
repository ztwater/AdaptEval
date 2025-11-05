import numpy as np
from talib import MAX, MIN

def PIVOTHIGH(high: np.ndarray, left:int, right: int):
    pivots = np.roll(MAX(high, left + 1 + right), -right)
    pivots[pivots != high] = np.NaN
    return pivots

def PIVOTLOW(low: np.ndarray, left:int, right: int):
    pivots = np.roll(MIN(low, left + 1 + right), -right)
    pivots[pivots != low] = np.NaN
    return pivots
