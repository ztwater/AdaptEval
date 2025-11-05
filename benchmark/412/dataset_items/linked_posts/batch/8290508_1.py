data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list of data 

for x in batch(data, 3):
    print(x)

# Output

[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[9, 10]
