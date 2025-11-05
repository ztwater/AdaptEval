def cache(fn=None,time_to_live=3600*24): # one DAY default (or whatever)
    if not fn: return functools.partial(cache,time_to_live=time_to_live)
    my_cache = {}
    def _inner_fn(*args,**kwargs)
        kws = sorted(kwargs.items()) # in python3.6+ you dont need sorted
        key = tuple(args)+tuple(kw) 
        if key not in my_cache or time.time() > my_cache[key]['expires']:
               my_cache[key] = {"value":fn(*args,**kwargs),"expires":time.time()+ time_to_live}
        return my_cache[key]
    return __inner_fn

@cache(time_to_live=3600) # an hour
def my_sqrt(x):
    return x**0.5

@cache(time_to_live=60*30) # 30 mins
def get_new_emails():
    return my_stmp.get_email_count()
