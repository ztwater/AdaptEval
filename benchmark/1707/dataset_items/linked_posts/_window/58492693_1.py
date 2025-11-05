win_list = []
for win_start_idx in range(n):
    win_end_idx = (len(seq) - n + 1 + i)
    win_list.append(seq[win_start_idx:win_end_idx])
win_list = zip(*win_list)  # transpose rows of columns to columns of rows
