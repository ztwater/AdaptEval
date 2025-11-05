import pandas as pd

#led to error:
df.to_csv('my_file.pkl')

#correct way:
df.to_pickle('my_file.pkl')
