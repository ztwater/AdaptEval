def divide_list_to_chunks(list_, n):
    return [list_[start::n] for start in range(n)]
