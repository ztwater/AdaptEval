>>> import re
>>> sorted(lst, key=lambda x: int(re.findall(r'\d+$', x)[0]))
['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
