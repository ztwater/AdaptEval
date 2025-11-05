from joblib import Parallel, delayed  
import multiprocessing


def Get_Corr_Mask(sp_mat, thresh, n_jobs=-1):
    
    # we must make sure the matrix is in csc format 
    # before we start doing all these column slices!  
    sp_mat = sp_mat.tocsc()
    cols = sp_mat.shape[1]
    
    if n_jobs == -1:
        # Process the work on all available CPU cores
        num_cores = multiprocessing.cpu_count()
    else:
        # Process the work on the specified number of CPU cores
        num_cores = n_jobs

    # Return a mask of all columns to keep by calling get_corr_row() 
    # once for each column in the matrix     
    return Parallel(n_jobs=num_cores, verbose=5)(delayed(get_corr_row)(i, sp_mat, thresh)for i in range(cols))
