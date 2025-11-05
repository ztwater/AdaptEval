def get_corr_row(idx_num, sp_mat, thresh):
    # slice the column at idx_num
    cols = sp_mat.shape[1]
    x = sp_mat[:,idx_num].toarray().ravel()
    start = idx_num + 1
    
    # Now slice each column to the right of idx_num   
    for i in range(start, cols):
        y = sp_mat[:,i].toarray().ravel()
        # Check the pearson correlation
        corr, pVal = pearsonr(x,y)
        # Pearson ranges from -1 to 1.
        # We check both positive and negative correlations >= thresh using abs(corr)
        if abs(corr) >= thresh:
            # stop checking after finding the 1st correlation > thresh   
            return False
            # Mark column at idx_num for removal in the mask  
    return True  
    
