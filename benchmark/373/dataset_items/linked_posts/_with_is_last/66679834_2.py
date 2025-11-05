for num_remaining, item in rev_enumerate(['a', 'b', 'c']):
    if num_remaining:
        print(f'This is NOT the last item in the list: {item}')
