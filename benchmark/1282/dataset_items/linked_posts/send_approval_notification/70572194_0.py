l=[]
for t in range(10):
    def up(y):
        print(y)
    l.append(up)
l[5]('printing in 5th function')
