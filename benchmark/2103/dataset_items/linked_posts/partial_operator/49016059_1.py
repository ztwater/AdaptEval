def bind_skip_first(func, *args, **kwargs):
  return lambda first: func(first, *args, **kwargs)

pow_two = bind_skip_first(pow, 2)
print(pow_two(3))  # 9
