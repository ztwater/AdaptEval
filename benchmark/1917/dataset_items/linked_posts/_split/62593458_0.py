import numpy as np

data # your array

total_length = len(data)
separate = 10
sub_array_size = total_length // separate
safe_separate = sub_array_size * separate

splited_lists = np.split(np.array(data[:safe_separate]), separate)
splited_lists[separate - 1] = np.concatenate(splited_lists[separate - 1], 
np.array(data[safe_separate:total_length]))

splited_lists # your output
