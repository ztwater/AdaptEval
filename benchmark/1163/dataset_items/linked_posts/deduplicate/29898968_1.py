default = (list(), set())
# use list to keep order
# use set to make lookup faster

def reducer(result, item):
    if item not in result[1]:
        result[0].append(item)
        result[1].add(item)
    return result

>>> reduce(reducer, l, default)[0]
[5, 6, 1, 2, 3, 4]
