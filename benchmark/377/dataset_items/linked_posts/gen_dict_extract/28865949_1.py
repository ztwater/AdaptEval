>>> findMe = {'Me':{'a':2,'Me':'bop'},'z':{'Me':4}}
>>> keyHole('Me',findMe)
<generator object keyHole at 0x105eccb90>
>>> [ x for x in keyHole('Me',findMe) ]
['bop', 4]
