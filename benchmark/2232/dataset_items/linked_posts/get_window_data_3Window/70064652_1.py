import pandas as pd
import numpy as np

index_slice = list(range(50,150)) # know index location for our inteterest
data = np.zeros(10000)
data[(index_slice)] = np.random.random(len(index_slice))

df = pd.DataFrame(
    {'column_name': data},
)

threshold = 0.5

