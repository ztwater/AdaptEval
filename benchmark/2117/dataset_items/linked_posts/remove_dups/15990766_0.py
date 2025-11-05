sequence = ['1', '2', '3', '3', '6', '4', '5', '6']
unique = []
[unique.append(item) for item in sequence if item not in unique]
