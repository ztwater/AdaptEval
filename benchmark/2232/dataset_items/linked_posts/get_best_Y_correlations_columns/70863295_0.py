def corr_cols(df,thresh):
    # Create correlation matrix
    corr_matrix = df.corr().abs()
    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_))

    dic = {'Feature_1':[],'Featur_2':[],'val':[]}
    for col in upper.columns:
        corl = list(filter(lambda x: x >= thresh, upper[col] ))
        #print(corl)
        if len(corl) > 0:
            inds = [round(x,4) for x in corl]
            for ind in inds:
                #print(col)
                #print(ind)
                col2 = upper[col].index[list(upper[col].apply(lambda x: round(x,4))).index(ind)]
                #print(col2)
                dic['Feature_1'].append(col)
                dic['Featur_2'].append(col2)
                dic['val'].append(ind) 
    return pd.DataFrame(dic).sort_values(by="val", ascending=False)
