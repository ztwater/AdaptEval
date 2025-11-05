from statsmodels.stats.weightstats import DescrStatsW
wq = DescrStatsW(data=np.array([1, 2, 9, 3.2, 4]), weights=np.array([0.0, 0.5, 1.0, 0.3, 0.5]))
wq.quantile(probs=np.array([0.1, 0.9]), return_pandas=False)
# array([2., 9.])
