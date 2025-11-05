def from_numpy_datetime_extract(date: np.datetime64, extract_attribute: str = None):
    _YEAR_OFFSET = 1970
    _MONTH_OFFSET = 1
    _MONTH_FACTOR = 12
    _DAY_FACTOR = 24*60*60*1e9
    _DAY_OFFSET = 1

    if extract_attribute == 'year':
        return date.astype('datetime64[Y]').astype(int) + _YEAR_OFFSET
    elif extract_attribute == 'month':
        return date.astype('datetime64[M]').astype(int)%_MONTH_FACTOR + _MONTH_OFFSET
    elif extract_attribute == 'day':
        return ((date - date.astype('datetime64[M]'))/_DAY_FACTOR).astype(int) + _DAY_OFFSET
    else:
        raise ValueError("extract_attribute should be either of 'year', 'month' or 'day'")
