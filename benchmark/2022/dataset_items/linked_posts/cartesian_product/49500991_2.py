a = np.arange(1000)
b = np.arange(200)

start = datetime.datetime.now()

foo = ((x,y) for x in a for y in b)

print (list(foo))

print ('execution time: {} s'.format((datetime.datetime.now() - start).total_seconds()))
