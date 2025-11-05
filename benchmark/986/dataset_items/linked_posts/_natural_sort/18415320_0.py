>>> from natsort import natsorted, ns
>>> x = ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
>>> natsorted(x, key=lambda y: y.lower())
['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
>>> natsorted(x, alg=ns.IGNORECASE)  # or alg=ns.IC
['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
