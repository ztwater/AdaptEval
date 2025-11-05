>>> from natsort import natsort_keygen, ns
>>> l1 = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
>>> l2 = l1[:]
>>> natsort_key1 = natsort_keygen(key=lambda y: y.lower())
>>> l1.sort(key=natsort_key1)
>>> l1
['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
>>> natsort_key2 = natsort_keygen(alg=ns.IGNORECASE)
>>> l2.sort(key=natsort_key2)
>>> l2
['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
