from scipy import stats
from matplotlib import pyplot as plt

# a normal distribution with a mean of 0 and standard deviation of 1
n = stats.norm(loc=0, scale=1)

# draw some random samples from it
sample = n.rvs(100)

# compute the ECDF of the samples
qe, pe = ecdf(sample)

# evaluate the theoretical CDF over the same range
q = np.linspace(qe[0], qe[-1], 1000)
p = n.cdf(q)

# plot
fig, ax = plt.subplots(1, 1)
ax.hold(True)
ax.plot(q, p, '-k', lw=2, label='Theoretical CDF')
ax.plot(qe, pe, '-r', lw=2, label='Empirical CDF')
ax.set_xlabel('Quantile')
ax.set_ylabel('Cumulative probability')
ax.legend(fancybox=True, loc='right')

plt.show()
