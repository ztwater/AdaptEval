def GetShiftingWindows(thelist, size):
    return [ thelist[x:x+size] for x in range( len(thelist) - size + 1 ) ]

>> a = [1, 2, 3, 4, 5]
>> GetShiftingWindows(a, 3)
[ [1, 2, 3], [2, 3, 4], [3, 4, 5] ]
