def primeSieveSeq(MAX_Int):
    if MAX_Int > 5*10**8:
        import ctypes
        int16Array = ctypes.c_ushort * (MAX_Int >> 1)
        sieve = int16Array()
        #print 'uses ctypes "unsigned short int Array"'
    else:
        sieve = (MAX_Int >> 1) * [False]
        #print 'uses python list() of long long int'
    if MAX_Int < 10**8:
        sieve[4::3] = [True]*((MAX_Int - 8)/6+1)
        sieve[12::5] = [True]*((MAX_Int - 24)/10+1)
    r = [2, 3, 5]
    n = 0
    for i in xrange(int(MAX_Int**0.5)/30+1):
        n += 3
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 2
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 1
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 2
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 1
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 2
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 3
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
        n += 1
        if not sieve[n]:
            n2 = (n << 1) + 1
            r.append(n2)
            n2q = (n2**2) >> 1
            sieve[n2q::n2] = [True]*(((MAX_Int >> 1) - n2q - 1) / n2 + 1)
    if MAX_Int < 10**8:
        return [2, 3, 5]+[(p << 1) + 1 for p in [n for n in xrange(3, MAX_Int >> 1) if not sieve[n]]]
    n = n >> 1
    try:
        for i in xrange((MAX_Int-2*n)/30 + 1):
            n += 3
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 2
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 1
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 2
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 1
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 2
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 3
            if not sieve[n]:
                r.append((n << 1) + 1)
            n += 1
            if not sieve[n]:
                r.append((n << 1) + 1)
    except:
        pass
    return r
