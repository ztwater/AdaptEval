def torch_compute_confidence_interval(data: Tensor,
                                      confidence: float = 0.95
                                      ) -> Tensor:
    """
    Computes the confidence interval for a given survey of a data set.
    """
    n: int = len(data)
    mean: Tensor = data.mean()
    # se: Tensor = scipy.stats.sem(data)  # compute standard error
    # se, mean: Tensor = torch.std_mean(data, unbiased=True)  # compute standard error
    se: Tensor = data.std(unbiased=True) / (n ** 0.5)
    t_p: float = float(scipy.stats.t.ppf((1 + confidence) / 2., n - 1))
    ci = t_p * se
    return mean, ci
