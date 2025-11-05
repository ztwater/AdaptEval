i = 0
out = []
for it in paged_iter(data,5)
    if (i % 2 == 0):
         swapped = it
    else: 
         out += list(it)
         out += list(swapped)
    i = i + 1
