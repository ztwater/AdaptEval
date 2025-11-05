>>> f = sys._current_frames().values()[0]
>>> # for python3: f = list(sys._current_frames().values())[0]

>>> print f.f_back.f_globals['__file__']
'/base/data/home/apps/apricot/1.6456165165151/caller.py'

>>> print f.f_back.f_globals['__name__']
'__main__'
