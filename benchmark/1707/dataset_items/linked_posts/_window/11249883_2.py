import itertools as it
def window4(iterable, size):
    complete_itr, incomplete_itr = it.tee(iterable, 2)
    iters = [complete_itr]
    for i in xrange(1, size):
        incomplete_itr.next()
        complete_itr, incomplete_itr = it.tee(incomplete_itr, 2)
        iters.append(complete_itr)
    return it.izip(*iters)
