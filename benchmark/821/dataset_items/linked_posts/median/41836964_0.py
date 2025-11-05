def median(*arg):
    order(arg)
    numArg = len(arg)
    half = int(numArg/2)
    if numArg/2 ==half:
        print((arg[half-1]+arg[half])/2)
    else:
        print(int(arg[half]))

def order(tup):
    ordered = [tup[i] for i in range(len(tup))]
    test(ordered)
    while(test(ordered)):
        test(ordered)
    print(ordered)


def test(ordered):
    whileloop = 0 
    for i in range(len(ordered)-1):
        print(i)
        if (ordered[i]>ordered[i+1]):
            print(str(ordered[i]) + ' is greater than ' + str(ordered[i+1]))
            original = ordered[i+1]
            ordered[i+1]=ordered[i]
            ordered[i]=original
            whileloop = 1 #run the loop again if you had to switch values
    return whileloop
