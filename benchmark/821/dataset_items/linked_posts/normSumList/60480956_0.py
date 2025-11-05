import pandas as pd


raw = [0.07, 0.14, 0.07]  

raw_df = pd.DataFrame(raw)
normed_df = raw_df.div(raw_df.sum(axis=0), axis=1)
normed_df
