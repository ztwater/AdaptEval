In [9]: a = range(10,14)

In [10]: mean_confidence_interval(a)
Out[10]: (11.5, 9.4457397432391215, 13.554260256760879)

In [11]: st.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=st.sem(a))
Out[11]: (9.4457397432391215, 13.554260256760879)

In [12]: sms.DescrStatsW(a).tconfint_mean()
Out[12]: (9.4457397432391197, 13.55426025676088)
