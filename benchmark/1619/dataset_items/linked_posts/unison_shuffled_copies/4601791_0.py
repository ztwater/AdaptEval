for old_index in len(a):
    new_index = numpy.random.randint(old_index+1)
    a[old_index], a[new_index] = a[new_index], a[old_index]
    b[old_index], b[new_index] = b[new_index], b[old_index]
