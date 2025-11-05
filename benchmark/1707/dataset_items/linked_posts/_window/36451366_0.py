mylist = [1, 2, 3, 4, 5, 6, 7]

def sliding_window(l, window_size=2):
    if window_size > len(l):
        raise ValueError("Window size must be smaller or equal to the number of elements in the list.")

    t = []
    for i in xrange(0, window_size):
        t.append(l[i:])

    return zip(*t)

print sliding_window(mylist, 3)
