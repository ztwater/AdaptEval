df['distance'] = pairwise_distances(df[['feat1', 'feat2']],
                                    df.loc[0:0, ['feat1', 'feat2']])
df
