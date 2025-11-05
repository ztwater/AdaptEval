import pandas as pd
import numpy as np
import io

df = pd.read_table(io.StringIO("""
y_train     feat1   feat2
0   9.596113    -7.900107
1   -1.384157   2.685313
2   -8.211954   5.214797
"""), sep=r"\s+")

df[['feat1', 'feat2']].to_numpy()
