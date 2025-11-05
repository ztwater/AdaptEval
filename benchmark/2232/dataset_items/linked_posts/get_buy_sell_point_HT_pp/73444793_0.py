pivots = high_column.shift(-len_right, fill_value=0).rolling(len_left).max()
