def cache(time_to_live=3600*24): # one DAY default (or whatever)
    def _wrap(fn):
        my_cache = {}
        def _inner_fn(*args,**kwargs)
            kws = sorted(kwargs.items()) # in python3.6+ you dont need sorted
            key = tuple(args)+tuple(kw) 
            if key not in my_cache or time.time() > my_cache[key]['expires']:
                 my_cache[key] = {"value":fn(*args,**kwargs),"expires":time.time()+ time_to_live}
            return my_cache[key]
         return _inner_fn
    return _wrap
