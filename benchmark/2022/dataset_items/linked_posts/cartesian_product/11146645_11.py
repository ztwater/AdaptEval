>>> def repeat_product(x, y):
...     return numpy.transpose([numpy.tile(x, len(y)), 
                                numpy.repeat(y, len(x))])
...
>>> def dstack_product(x, y):
...     return numpy.dstack(numpy.meshgrid(x, y)).reshape(-1, 2)
...     
