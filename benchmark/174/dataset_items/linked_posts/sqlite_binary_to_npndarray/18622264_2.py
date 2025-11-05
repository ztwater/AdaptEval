cur.execute("select arr from test")
data = cur.fetchone()[0]

print(data)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]
print(type(data))
# <type 'numpy.ndarray'>
