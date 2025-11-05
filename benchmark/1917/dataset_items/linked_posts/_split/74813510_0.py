def splitList(lst, into):
    '''Split a list into parts.

    :Parameters:
        into (str) = Split the list into parts defined by the following:
            '<n>parts' - Split the list into n parts.
                ex. 2 returns:  [[1, 2, 3, 5], [7, 8, 9]] from [1,2,3,5,7,8,9]
            '<n>parts+' - Split the list into n equal parts with any trailing remainder.
                ex. 2 returns:  [[1, 2, 3], [5, 7, 8], [9]] from [1,2,3,5,7,8,9]
            '<n>chunks' - Split into sublists of n size.
                ex. 2 returns: [[1,2], [3,5], [7,8], [9]] from [1,2,3,5,7,8,9]
            'contiguous' - The list will be split by contiguous numerical values.
                ex. 'contiguous' returns: [[1,2,3], [5], [7,8,9]] from [1,2,3,5,7,8,9]
            'range' - The values of 'contiguous' will be limited to the high and low end of each range.
                ex. 'range' returns: [[1,3], [5], [7,9]] from [1,2,3,5,7,8,9]
    :Return:
        (list)
    '''
    from string import digits, ascii_letters, punctuation
    mode = into.lower().lstrip(digits)
    digit = into.strip(ascii_letters+punctuation)
    n = int(digit) if digit else None

    if n:
        if mode=='parts':
            n = len(lst)*-1 // n*-1 #ceil
        elif mode=='parts+':
            n = len(lst) // n
        return [lst[i:i+n] for i in range(0, len(lst), n)]

    elif mode=='contiguous' or mode=='range':
        from itertools import groupby
        from operator import itemgetter

        try:
            contiguous = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(lst), lambda x: int(x[0])-int(x[1]))]
        except ValueError as error:
            print ('{} in splitList\n   # Error: {} #\n {}'.format(__file__, error, lst))
            return lst
        if mode=='range':
            return [[i[0], i[-1]] if len(i)>1 else (i) for i in contiguous]
        return contiguous

r = splitList([1, '2', 3, 5, '7', 8, 9], into='2parts')
print (r) #returns: [[1, '2', 3, 5], ['7', 8, 9]]
