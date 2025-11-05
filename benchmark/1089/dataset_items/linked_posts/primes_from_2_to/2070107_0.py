def daniel_sieve_2(maxNumber):
    """
    Given a number, returns all numbers less than or equal to
    that number which are prime.
    """
    allNumbers = range(3, maxNumber+1, 2)
    for mIndex, number in enumerate(xrange(3, maxNumber+1, 2)):
        if allNumbers[mIndex] == 0:
            continue
        # now set all multiples to 0
        for index in xrange(mIndex+number, (maxNumber-3)/2+1, number):
            allNumbers[index] = 0
    return [2] + filter(lambda n: n!=0, allNumbers)
