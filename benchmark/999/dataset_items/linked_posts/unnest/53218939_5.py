s.join(df.drop('B',1),how='left').reindex(columns=df.columns)
