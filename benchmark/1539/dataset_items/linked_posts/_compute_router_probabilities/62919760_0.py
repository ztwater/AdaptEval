# generating uniform variables

import numpy as np

num_samples = 3
Din = 1
lb, ub = -1, 1

xn = np.random.uniform(low=lb, high=ub, size=(num_samples,Din))
print(xn)

import torch

sampler = torch.distributions.Uniform(low=lb, high=ub)
r = sampler.sample((num_samples,Din))

print(r)

r2 = torch.torch.distributions.Uniform(low=lb, high=ub).sample((num_samples,Din))

print(r2)

# process input
f = nn.Sequential(OrderedDict([
    ('f1', nn.Linear(Din,Dout)),
    ('out', nn.SELU())
]))
Y = f(r2)
print(Y)
