#use a dict comprehension. Adding {} in get() is to set a default return value if the key doesn't exist in dict1

{k:dict(dict1.get(k,{}).items() + v.items()) for k,v in dict2.items()}
Out[689]: {'employee': {'dev1': 'Roy', 'dev2': 'Biswas'}}

#Alternatively, a less readable way to merge the dicts using the dict constructor.

{k:dict(dict1.get(k,{}), **v) for k,v in dict2.items()}
Out[690]: {'employee': {'dev1': 'Roy', 'dev2': 'Biswas'}}
