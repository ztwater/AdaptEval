import torch
from torch.distributions import uniform

distribution = uniform.Uniform(torch.Tensor([0.0]),torch.Tensor([5.0]))
distribution.sample(torch.Size([2,3])
