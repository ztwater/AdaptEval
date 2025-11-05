import torch as pt
pt.empty(2,3).uniform_(5,10).type(pt.FloatTensor)
