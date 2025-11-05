>>> from naapc import NDict
>>> dict1 = NDict({'employee':{'dev1': 'Roy'}})
>>> dict2 = {'employee':{'dev2': 'Biswas'}}
>>> dict1.update(dict2)
>>> print(dict1)
{
  "employee": {
    "dev1": "Roy",
    "dev2": "Biswas"
  }
}
