def get_pivot_high(ohlcvs: List[OHLCV], left_bars: int, right_bars: int, key_name: str = 'high_price') -> Optional[float]:
    if len(ohlcvs) < left_bars + right_bars:
        return None
    highest_value = max(ohlcv.get(key_name) for ohlcv in ohlcvs[-(left_bars + right_bars + 1):])
    return highest_value if highest_value == ohlcvs[-right_bars].get(key_name) else None
