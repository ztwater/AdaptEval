def chunkify(target_list, chunk_size):
    return [target_list[i:i+chunk_size] for i in range(0, len(target_list), chunk_size)]

>>> l = [5432, 432, 67, "fdas", True, True, False, (4324,131), 876, "ofsa", 8, 909, b'765']
>>> print(chunkify(l, 3))
>>> [[5432, 432, 67], ['fdas', True, True], [False, (4324, 131), 876], ['ofsa', 8, 909], [b'765']]
