    corr = corr_cols(star,0.5)
    df.drop(columns = corr.iloc[:,0].unique())
