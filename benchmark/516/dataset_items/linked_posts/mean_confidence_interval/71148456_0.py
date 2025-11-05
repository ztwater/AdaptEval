import numpy as np

def mean_confidence_interval(data, confidence: float = 0.95) -> tuple[float, np.ndarray]:
    """
    Returns (tuple of) the mean and confidence interval for given data.
    Data is a np.arrayable iterable.

    ref:
        - https://stackoverflow.com/a/15034143/1601580
        - https://github.com/WangYueFt/rfs/blob/f8c837ba93c62dd0ac68a2f4019c619aa86b8421/eval/meta_eval.py#L19
    """
    import scipy.stats
    import numpy as np

    a: np.ndarray = 1.0 * np.array(data)
    n: int = len(a)
    if n == 1:
        import logging
        logging.warning('The first dimension of your data is 1, perhaps you meant to transpose your data? or remove the'
                        'singleton dimension?')
    m, se = a.mean(), scipy.stats.sem(a)
    tp = scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    h = se * tp
    return m, h

def ci_test_float():
    import numpy as np
    # - one WRONG data set of size 1 by N
    data = np.random.randn(1, 30)  # gives an error becuase len sets n=1, so not this shape!
    m, ci = mean_confidence_interval(data)
    print('-- you should get a mean and a list of nan ci (since data is in wrong format, it thinks its 30 data sets of '
          'length 1.')
    print(m, ci)

    # right data as N by 1
    data = np.random.randn(30, 1)
    m, ci = mean_confidence_interval(data)
    print('-- gives a mean and a list of length 1 for a single CI (since it thinks you have a single dat aset)')
    print(m, ci)

    # multiple data sets (7) of size N (=30)
    data = np.random.randn(30, 7)
    print('-- gives 7 CIs for the 7 data sets of length 30. 30 is the number ud want large if you were using z(p)'
          'due to the CLT.')
    m, ci = mean_confidence_interval(data)
    print(m, ci)

ci_test_float()
