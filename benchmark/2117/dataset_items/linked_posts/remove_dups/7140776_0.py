def f7_noHash(seq)
    seen = set()
    return [ x for x in seq if str( x ) not in seen and not seen.add( str( x ) )]
