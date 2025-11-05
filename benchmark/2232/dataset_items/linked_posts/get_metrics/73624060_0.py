def corr_cleaner(df,corr_cutoff):
    '''
    df: pandas dataframe with column headers.
    corr_cutoff: float between 0 and 1.
    '''
    abs_corr_matrix = df.corr().abs()
    filtered_cols = []
    while True:
        offenders = []
        for i in range(len(abs_corr_matrix)):
            for j in range(len(abs_corr_matrix)):
                if i != j:
                    if abs_corr_matrix.iloc[i,j] > corr_cutoff:
                        offenders.append(df.columns[i])

        if len(offenders) > 0: # if at least one high correlation remains
            c = Counter(offenders)
            worst_offender = c.most_common(1)[0][0]  # var name of worst offender
            del df[worst_offender]
            filtered_cols.append(worst_offender)
            abs_corr_matrix.drop(worst_offender, axis=0, inplace=True) #drop from x-axis
            abs_corr_matrix.drop(worst_offender, axis=1, inplace=True) #drop from y-axis
        else: # if no high correlations remain, break
            break

    return df, filtered_cols
