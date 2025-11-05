from dict-path import DictPath

data_dict = {
  "foo1": "bar1",
  "foo2": "bar2",
  "foo3": {
     "foo4": "bar4",
     "foo5": {
        "foo6": "bar6",
        "foo7": "bar7",
     },
  }
}

data_dict_path = DictPath(data_dict)
data_dict_path.get('key1/key2/key3')
