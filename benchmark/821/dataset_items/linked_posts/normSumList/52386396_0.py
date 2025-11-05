import random, time
import numpy as np

a = random.sample(range(1, 20000), 10000)
since = time.time(); b = [i/sum(a) for i in a]; print(time.time()-since)
# 0.7956490516662598

since = time.time(); c=np.array(a);d=c/sum(a); print(time.time()-since)
# 0.001413106918334961
