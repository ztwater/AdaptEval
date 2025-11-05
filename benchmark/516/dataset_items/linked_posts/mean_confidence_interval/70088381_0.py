from scipy.stats import norm
alpha = 0.95
# Define our z
ci = alpha + (1-alpha)/2
#Lower Interval, where n is sample siz
c_lb = sample_mean - norm.ppf(ci)*((sigma/(n**0.5)))
c_ub = sample_mean + norm.ppf(ci)*((sigma/(n**0.5)))
