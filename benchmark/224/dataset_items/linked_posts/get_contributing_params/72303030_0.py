import torch
import torch.nn as nn
# Example of a simple network
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.x = nn.Parameter(torch.tensor([999999.0]))  # not contributing
        self.layers = nn.ModuleList([nn.Sequential(nn.Linear(1, 4), nn.Linear(4, 1)) for _ in range(3)])
    def forward(self, x):
        for m in self.layers: x = m(x) + x
        return x

net = Net()
x = torch.ones((1, 1))
# compute the forward pass to create the computation graph
y = net(x)

# use computation graph to find all contributing tensors
def get_contributing_params(y, top_level=True):
    nf = y.grad_fn.next_functions if top_level else y.next_functions
    for f, _ in nf:
        try:
            yield f.variable
        except AttributeError:
            pass  # node has no tensor
        if f is not None:
            yield from get_contributing_params(f, top_level=False)

contributing_parameters = set(get_contributing_params(y))
all_parameters = set(net.parameters())
non_contributing = all_parameters - contributing_parameters
print(non_contributing)  # returns the [999999.0] tensor
