levels = map(tuple, frame.index.levels)
index = list(product(*levels))
frame = frame.reindex(index)
print(frame)
