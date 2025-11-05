    import numpy as np 
    from numba import jit
    
    @jit(nopython=True)
    def corr_filter(X, threshold):
        n = X.shape[1]
        columns = np.ones((n,))
        for i in range(n-1):
            for j in range(i+1, n):
                if columns[j] == 1:
                    correlation = np.abs(np.corrcoef(X[:,i], X[:,j])[0,1])
                    if correlation >= threshold:
                        columns[j] = 0
        return columns
    
    columns = corr_filter(df.values, 0.7).astype(bool) 
    selected_columns = df.columns[columns]
