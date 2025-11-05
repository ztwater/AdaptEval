import time 
lastResultCache = {}
resultCache = {}
def result_cacher(val):
    #.get() gets value for key from dict, but if the key is not in the dict, it returns 0
    if time.time() - lastResultCache.get(val, 0) >= 3600: #Checks if 3600 sec (1 hour) has passed since the last cache 
        lastResultCache[val] = time.time()
        resultCache[val] = result(val)
    return resultCache.get(val)
