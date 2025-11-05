class A: a = 1
x = A()
y = x
x.a = 5
print(y.a) #return's 5
