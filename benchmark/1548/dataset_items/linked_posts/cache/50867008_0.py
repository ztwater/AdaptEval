import time 
lastResultCache = 0 
resultCache = None
def result_cacher():
    if time.time() - lastResultCache >= 3600: #Checks if 3600 sec (1 hour) has passed since the last cache 
        lastResultCache = time.time()
        resultCache = result()
    return resultCache 
