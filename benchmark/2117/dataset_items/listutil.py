def remove_dups(seq: list):
    seen = set()  # type: ignore[var-annotated]
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
