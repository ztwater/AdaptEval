def get_pivot_low(ohlcvs: List[OHLCV], left_bars: int, right_bars: int, key_name: str = 'low_price') -> Optional[float]:
    if len(ohlcvs) < left_bars + right_bars:
        return None
    lowest_value = min(ohlcv.get(key_name) for ohlcv in ohlcvs[-(left_bars + right_bars + 1):])
    return lowest_value if lowest_value == ohlcvs[-right_bars].get(key_name) else None
