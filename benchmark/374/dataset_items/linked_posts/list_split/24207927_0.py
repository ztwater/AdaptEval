def chunkify(lst,n):
    [ lst[i::n] for i in xrange(n if n < len(lst) else len(lst)) ]
