TTL = 60 * 60 # one hour
cache = Cache(TTL)
cache.insert(key, value)

# check again after an hour

if key in cache:
    print(cache[key])
