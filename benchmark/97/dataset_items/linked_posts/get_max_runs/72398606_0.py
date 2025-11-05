import numpy as np
a = np.array([3, 3, 3, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3])
is_not_in_run = (a != 3)
is_not_in_run = np.concatenate(([True], is_not_in_run, [True]))
gap_indices = np.where(is_not_in_run)[0]
run_lengths = np.diff(gap_indices) - 1
run_lengths = np.delete(run_lengths, np.where(run_lengths == 0)[0])
print(run_lengths)
