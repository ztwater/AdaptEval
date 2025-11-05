frame.reindex(list(product(*map(tuple, frame.index.levels)))).values\
     .reshape(map(len, frame.index.levels))
