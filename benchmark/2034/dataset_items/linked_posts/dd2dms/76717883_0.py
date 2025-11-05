def dms_to_deg(dms):
    import math
    import numpy as np
    a=math.fabs(dms)
    d=a//10000
    m=(a-d*10000)//100
    s=(a-d*10000-m*100)
    deg=(d+m/60+s/3600)*np.sign(dms)
    return deg

#---Usage
r1=dms_to_deg(243055.25)
r2=dms_to_deg(-243055.25)
print(r1,r2)
