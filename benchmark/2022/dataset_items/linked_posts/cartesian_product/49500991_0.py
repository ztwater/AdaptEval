import numpy
import datetime
a = np.arange(1000)
b = np.arange(200)

start = datetime.datetime.now()

foo = (item for sublist in [list(map(lambda x: (x,i),a)) for i in b] for item in sublist)

print (list(foo))

print ('execution time: {} s'.format((datetime.datetime.now() - start).total_seconds()))
