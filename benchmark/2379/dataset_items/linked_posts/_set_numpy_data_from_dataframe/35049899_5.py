shape = map(len, frame.index.levels)
print(frame.values.reshape(shape))
