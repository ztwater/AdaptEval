>>> data = np.array([['a','b'],['c','d']])
# a 2D view
>>> data.view('S2')
array([['ab'],
       ['cd']], 
      dtype='|S2')
# or maybe a 1D view ...fastest solution:
>>> data.view('S2').ravel()
array(['ab', 'cd'], 
      dtype='|S2')
