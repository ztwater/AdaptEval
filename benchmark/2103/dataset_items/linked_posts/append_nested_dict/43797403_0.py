from collections import defaultdict

dict1 = {'employee': {'dev1': 'Roy'}, 'aKeyNotInDict2': {}}
dict2 = {'employee': {'dev2': 'Biswas'}, 'aKeyNotInDict1': {}}
merged_dict = defaultdict(dict)

merged_dict.update(dict1)
for key, nested_dict in dict2.items():
    merged_dict[key].update(nested_dict)

print(dict(merged_dict))
