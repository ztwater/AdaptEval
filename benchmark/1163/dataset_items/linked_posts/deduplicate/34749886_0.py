def deduplicate(l):
    count = {}
    (read,write) = (0,0)
    while read < len(l):
        if l[read] in count:
            read += 1
            continue
        count[l[read]] = True
        l[write] = l[read]
        read += 1
        write += 1
    return l[0:write]
