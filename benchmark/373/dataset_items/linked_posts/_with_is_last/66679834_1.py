for num_remaining, item in rev_enumerate(['a', 'b', 'c']):
    if not num_remaining:
        print(f'This is the last item in the list: {item}')
