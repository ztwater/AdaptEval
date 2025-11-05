import statsmodels.stats.api as sms
conf = sms.DescrStatsW(a).tconfint_mean(alpha=0.05)
conf
