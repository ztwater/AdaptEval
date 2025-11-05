from functools import reduce
def batch(input_list, batch_size):
  def reducer(cumulator, item):
    if len(cumulator[-1]) < batch_size:
      cumulator[-1].append(item)
      return cumulator
    else:
      cumulator.append([item])
    return cumulator
  return reduce(reducer, input_list, [[]])
