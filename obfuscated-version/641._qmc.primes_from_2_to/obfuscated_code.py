import numpy
def primesfrom2to(var_0):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    var_1 = numpy.ones(var_0//3 + (var_0%6==2), dtype=bool)
    for i in range(1,int(var_0**0.5)//3+1):
        if var_1[i]:
            var_2=3*i+1|1
            var_1[       var_2*var_2//3     ::2*var_2] = False
            var_1[var_2*(var_2-2*(i&1)+4)//3::2*var_2] = False
    return numpy.r_[2,3,((3*numpy.nonzero(var_1)[0][1:]+1)|1)]
