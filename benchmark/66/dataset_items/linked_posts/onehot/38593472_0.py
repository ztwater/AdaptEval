import time
start_time = time.time()
z=[]
for l in [1,2,3,4,5,6,1,2,3,4,4,6,]:
    a= np.repeat(0,10)
    np.put(a,l,1)
    z.append(a)
print("--- %s seconds ---" % (time.time() - start_time))

#--- 0.00174784660339 seconds ---

import time
start_time = time.time()
z=[]
for l in [1,2,3,4,5,6,1,2,3,4,4,6,]:
    z.append(np.array([int(i == l) for i in range(10)]))
print("--- %s seconds ---" % (time.time() - start_time))

#--- 0.000400066375732 seconds ---
