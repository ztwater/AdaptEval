import weightedcalcs as wc
import pandas as pd

df = pd.DataFrame({'v': [1, 2, 3], 'w': [3, 2, 1]})
calc = wc.Calculator('w')  # w designates weight

calc.quantile(df, 'v', 0.5)
# 1.5
