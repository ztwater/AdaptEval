def my_weighted_perc(data,perc,weights=None):
    if weights==None:
        return nanpercentile(data,perc)
    else:
        d=data[(~np.isnan(data))&(~np.isnan(weights))]
        ix=np.argsort(d)
        d=d[ix]
        wei=weights[ix]
        wei_cum=100.*cumsum(wei*1./sum(wei))
        return interp(perc,wei_cum,d)
