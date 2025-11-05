def rmdiacritics(var_0):
    '''
    Return the base character of char, by "removing" any
    diacritics like accents or curls and strokes and the like.
    '''
    var_1 = ud.name(var_0)
    var_2 = var_1.find(' WITH ')
    if var_2 != -1:
        var_1 = var_1[:var_2]
        try:
            var_0 = ud.lookup(var_1)
        except KeyError:
            pass  # removing "WITH ..." produced an invalid name
    return var_0
