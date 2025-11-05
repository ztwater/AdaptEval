def print_progressbar(total, current, barsize=60):
    progress = int(current*barsize/total)
    completed = str(int(current*100/total)) + '%'
    print('[', chr(9608)*progress, ' ', completed, '.'*(barsize-progress), '] ', str(i)+'/'+str(total), sep='', end='\r', flush=True)
