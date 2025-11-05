def batch(x, bs):
    return [x[i:i+bs] for i in range(0, len(x), bs)]
