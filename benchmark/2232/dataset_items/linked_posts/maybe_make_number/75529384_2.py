from random import choices, randint
from string import digits
from perfplot import plot
plot(
    setup=lambda n: [''.join(choices(digits, k=randint(1,10))) for _ in range(n)],
    kernels=[lambda lst: [int(x) for x in lst], lambda lst: list(map(int, lst))],
    labels= ["[int(x) for x in lst]", "list(map(int, lst))"],
    n_range=[2**k for k in range(4, 22)],
    xlabel='Number of items',
    title='Converting strings to integers',
    equality_check=lambda x,y: x==y);
