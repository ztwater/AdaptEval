from functools import reduce
reduce(lambda cumulator,item: cumulator[-1].append(item) or cumulator if len(cumulator[-1]) < batch_size else cumulator + [[item]], input_array, [[]])
