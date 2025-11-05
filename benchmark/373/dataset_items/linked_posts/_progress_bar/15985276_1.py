def update_progress(progress, total):  
    print('\r[{0:10}]{1:>2}%'.format('#' * int(progress * 10 /total), progress), end='')
