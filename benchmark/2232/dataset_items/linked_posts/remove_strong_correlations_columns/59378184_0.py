dropvars = []
threshold = 0.95
df_corr = df.corr().stack().reset_index().rename(columns={'level_0': 'Var 1', 'level_1': 'Var 2', 0: 'Corr'})
df_corr = df_corr[(df_corr['Corr'].abs() >= threshold) & (df_corr['Var 1'] != df_corr['Var 2'])]
while len(df_corr) > 0:
    var = df_corr['Var 1'].iloc[0]
    df_corr = df_corr[((df_corr['Var 1'] != var) & (df_corr['Var 2'] != var))]
    dropvars.append(var)
df.drop(columns=dropvars, inplace=True)
