def get_corr_feature(df):
    corr_matrix = df.corr().abs()
    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_))
    upper['score']= upper.max(axis=1)
    upper.sort_values(by=['score'],ascending=False)
    #Find the most correlated feature and send return it for drop
    column_name=upper.sort_values(by=['score'],ascending=False).index[0]
    max_score=upper.loc[column_name,'score']
    return column_name, max_score

max_score=1
while max_score>0.5:
    column_name, max_score=get_corr_feature(df)
    df.drop(column_name,axis=1,inplace=True)
