import time    
for i in range(2,10):
    timer =time.time()
    generate_primes(10**i)
    print('n = 10^',i,' time =', round(time.time()-timer,6))

>> n = 10^ 2  time = 5.6e-05
>> n = 10^ 3  time = 6.4e-05
>> n = 10^ 4  time = 0.000114
>> n = 10^ 5  time = 0.000593
>> n = 10^ 6  time = 0.00467
>> n = 10^ 7  time = 0.177758
>> n = 10^ 8  time = 1.701312
>> n = 10^ 9  time = 19.322478
