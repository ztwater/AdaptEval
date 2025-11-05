correlatedColumns = []
corr = df.corr()
indices = corr.index
columns = corr.columns
posthreshold = 0.7
negthreshold = -0.7

for c in columns:
    for r in indices:
        if c != r and (corr[c][r] > posthreshold or corr[c][r] < negthreshold):
            correlatedColumns.append({"column" : c , "row" : r , "val" :corr[c][r] })
            

print(correlatedColumns)
