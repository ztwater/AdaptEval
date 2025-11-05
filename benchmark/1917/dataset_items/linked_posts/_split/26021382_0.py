def chunks(l, amount):
    if amount < 1:
        raise ValueError('amount must be positive integer')
    chunk_len = len(l) // amount
    leap_parts = len(l) % amount
    remainder = amount // 2  # make it symmetrical
    i = 0
    while i < len(l):
        remainder += leap_parts
        end_index = i + chunk_len
        if remainder >= amount:
            remainder -= amount
            end_index += 1
        yield l[i:end_index]
        i = end_index
