def uniquefy_list(a):
    return uniquefy_list(a[1:]) if a[0] in a[1:] else [a[0]]+uniquefy_list(a[1:]) if len(a)>1 else [a[0]]
