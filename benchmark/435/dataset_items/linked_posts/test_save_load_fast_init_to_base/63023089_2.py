class A:a = 1
x = A()
y = copy(x)
x.a = 5
print(y.a) #return 1
