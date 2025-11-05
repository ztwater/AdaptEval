array = np.arange(100000)
val = array[50000]+0.55
print( bisection(array,val))
%timeit bisection(array,val)
print( find_nearest1(array,val))
%timeit find_nearest1(array,val)
print( find_nearest2(array,val))
%timeit find_nearest2(array,val)
print( find_nearest3(array,val))
%timeit find_nearest3(array,val)
print( find_nearest4(array,val))
%timeit find_nearest4(array,val)
print( find_nearest5(array,val))
%timeit find_nearest5(array,val)
print( find_nearest6(array,val))
%timeit find_nearest6(array,val)

(50000, 50000)
100000 loops, best of 3: 4.4 µs per loop
50001
1 loop, best of 3: 180 ms per loop
50001
1000 loops, best of 3: 267 µs per loop
[50000]
1000 loops, best of 3: 390 µs per loop
50001
1000 loops, best of 3: 259 µs per loop
50001
1000 loops, best of 3: 1.21 ms per loop
[50000]
1000 loops, best of 3: 746 µs per loop
