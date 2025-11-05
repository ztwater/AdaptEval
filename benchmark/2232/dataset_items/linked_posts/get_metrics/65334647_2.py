#Get the mask using your sparse matrix and threshold.
corr_mask = Get_Corr_Mask(X_t_fpr, 0.95) 

# Remove features that are >= 95% correlated
X_t_fpr_corr = X_t_fpr[:,corr_mask]
