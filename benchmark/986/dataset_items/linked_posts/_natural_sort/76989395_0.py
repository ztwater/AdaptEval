def sort_naturally(lst: list) -> list:
    max_str_len = max([len(s) for s in lst])
    return sorted(lst, key=lambda s: s.zfill(max_str_len + 1))
