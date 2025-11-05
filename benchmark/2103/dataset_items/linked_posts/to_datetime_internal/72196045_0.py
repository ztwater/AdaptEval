import numpy as np

date = np.datetime64("2000-01-01")
date_strings = date.astype(str).split('-'). 
# >> ['2000', '01', '01']

year_int = int(date_strings[0])
