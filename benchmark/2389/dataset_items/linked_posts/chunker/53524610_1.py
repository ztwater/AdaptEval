items = list(range(1,1251))

for item_group in iter_group(items, 1000):
    for item in item_group:
        print(item)
