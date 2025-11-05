seq = [0, 1, 2, 3, 4, 5]
window_size = 3

for i in range(len(seq) - window_size + 1):
    print(seq[i: i + window_size])
