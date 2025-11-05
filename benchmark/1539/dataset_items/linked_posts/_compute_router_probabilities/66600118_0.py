from torch.distributions.uniform import Uniform

shape = 3,4
r1, r2 = 0,1

x = Uniform(r1, r2).sample(shape) 
