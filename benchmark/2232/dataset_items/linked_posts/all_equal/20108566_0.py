lambda lst: reduce(lambda a,b:(b,b==a[0] and a[1]), lst, (lst[0], True))[1]
