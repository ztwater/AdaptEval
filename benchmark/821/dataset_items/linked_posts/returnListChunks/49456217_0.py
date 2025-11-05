def proportional_dividing(N, n):
    """
    N - length of array (bigger number)
    n - number of chunks (smaller number)
    output - arr, containing N numbers, diveded roundly to n chunks
    """
    arr = []
    if N == 0:
        return arr
    elif n == 0:
        arr.append(N)
        return arr
    r = N // n
    for i in range(n-1):
        arr.append(r)
    arr.append(N-r*(n-1))

    last_n = arr[-1]
    # last number always will be r <= last_n < 2*r
    # when last_n == r it's ok, but when last_n > r ...
    if last_n > r:
        # ... and if difference too big (bigger than 1), then
        if abs(r-last_n) > 1:
            #[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7] # N=29, n=12
            # we need to give unnecessary numbers to first elements back
            diff = last_n - r
            for k in range(diff):
                arr[k] += 1
            arr[-1] = r
            # and we receive [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2]
    return arr

def split_items(items, chunks):
    arr = proportional_dividing(len(items), chunks)
    splitted = []
    for chunk_size in arr:
        splitted.append(items[:chunk_size])
        items = items[chunk_size:]
    print(splitted)
    return splitted

items = [1,2,3,4,5,6,7,8,9,10,11]
chunks = 3
split_items(items, chunks)
split_items(['a','b','c','d','e','f','g','h','i','g','k','l', 'm'], 3)
split_items(['a','b','c','d','e','f','g','h','i','g','k','l', 'm', 'n'], 3)
split_items(range(100), 4)
split_items(range(99), 4)
split_items(range(101), 4)
