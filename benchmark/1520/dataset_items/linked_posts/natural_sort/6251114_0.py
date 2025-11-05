alist=["something1",
    "something12",
    "something17",
    "something2",
    "something25and_then_33",
    "something25and_then_34",
    "something29",
    "beta1.1",
    "beta2.3.0",
    "beta2.33.1",
    "a001",
    "a2",
    "z002",
    "z1"]

def key(k):
    nums=set(list("0123456789"))
        chars=set(list(k))
    chars=chars-nums
    for i in range(len(k)):
        for c in chars:
            k=k.replace(c+"0",c)
    l=list(k)
    base=10
    j=0
    for i in range(len(l)-1,-1,-1):
        try:
            l[i]=int(l[i])*base**j
            j+=1
        except:
            j=0
    l=tuple(l)
    print l
    return l

print sorted(alist,key=key)
