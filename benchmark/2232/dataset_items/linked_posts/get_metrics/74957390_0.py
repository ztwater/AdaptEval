from statsmodels.stats.outliers_influence import variance_inflation_factor

def vif(X):
    vif = pd.DataFrame()
    vif['Variables'] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif
