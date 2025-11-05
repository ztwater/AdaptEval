import pandas as pd

my_list = [0, 1, 2, 3, 4, 1, 2, 3, 5]

>>> pd.Series(my_list).drop_duplicates().tolist()
# Output:
# [0, 1, 2, 3, 4, 5]
