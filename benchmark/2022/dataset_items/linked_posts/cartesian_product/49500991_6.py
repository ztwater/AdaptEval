a = np.arange(1000)
b = np.arange(200)

start = datetime.datetime.now()

foo = np.dot(np.asmatrix([[i,0] for i in a]), np.asmatrix([[i,0] for i in b]).T)

print (foo)

print ('execution time: {} s'.format((datetime.datetime.now() - start).total_seconds()))
