df[['B', 'B2']] = pd.DataFrame(df['B'].values.tolist())

df[['A', 'B']].append(df[['A', 'B2']].rename(columns={'B2': 'B'}),
                      ignore_index=True)
