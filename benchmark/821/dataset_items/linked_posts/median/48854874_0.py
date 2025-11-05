def midme(list1):

    list1.sort()
    if len(list1)%2>0:
            x = list1[int((len(list1)/2))]
    else:
            x = ((list1[int((len(list1)/2))-1])+(list1[int(((len(list1)/2)))]))/2
    return x


midme([4,5,1,7,2])
