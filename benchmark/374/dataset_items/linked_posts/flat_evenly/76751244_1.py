flat_list = [e for tup in zip_longest(*list_of_lists) for e in tup if e is not None]
