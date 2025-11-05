reduce(lambda x, y: x + y if y[0] not in x else x, map(lambda x: [x],lst))
