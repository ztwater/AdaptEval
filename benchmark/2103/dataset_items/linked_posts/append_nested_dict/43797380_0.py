>>> dict1 = {'employee':{'dev1': 'Roy'}}
>>> dict2 = {'employee':{'dev2': 'Biswas'}}
>>> 
>>> for key in dict1:
...     if key in dict2:
...         dict1[key].update(dict2[key])
... 
>>> dict1
{'employee': {'dev2': 'Biswas', 'dev1': 'Roy'}}
