for index, element in enumerate(sequence):
    if index == len(sequence) - 1:
        do_something_special(element)
    else:
        do_something_normal(element)
