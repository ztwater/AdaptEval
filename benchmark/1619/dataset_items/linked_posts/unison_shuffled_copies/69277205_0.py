random.seed(seed)
random.shuffle(x_data)
# reset the same seed to get the identical random sequence and shuffle the y
random.seed(seed)
random.shuffle(y_data)
