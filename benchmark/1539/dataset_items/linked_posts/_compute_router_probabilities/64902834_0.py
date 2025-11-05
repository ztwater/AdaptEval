import torch
a,b = 2,3   #dimension of the pytorch tensor to be generated
low,high = 0,1 #range of uniform distribution

x = torch.distributions.uniform.Uniform(low,high).sample([a,b]) 
