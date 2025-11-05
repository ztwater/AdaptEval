# Show off random range.
print()
for v in range(3,6):
    v = 2**v
    l = list(random_range(v))
    print("Need",v,"found",len(set(l)),"(min,max)",(min(l),max(l)))
    print("",l)
    print()
