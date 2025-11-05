def quantile_at_values(values, population, weights=None):
    values = numpy.atleast_1d(values).astype(float)
    population = numpy.atleast_1d(population).astype(float)
    # if no weights are given, use equal weights
    if weights is None:
        weights = numpy.ones(population.shape).astype(float)
        normal = float(len(weights))
    # else, check weights                  
    else:                                           
        weights = numpy.atleast_1d(weights).astype(float)
        assert len(weights) == len(population)
        assert (weights >= 0).all()
        normal = numpy.sum(weights)                    
        assert normal > 0.
    quantiles = numpy.array([numpy.sum(weights[population <= value]) for value in values]) / normal
    assert (quantiles >= 0).all() and (quantiles <= 1).all()
    return quantiles
