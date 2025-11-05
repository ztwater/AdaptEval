import numpy as np
def find_nearest(array, value):
    array = np.array(array)
    z=np.abs(array-value)
    y= np.where(z == z.min())
    m=np.array(y)
    x=m[0,0]
    y=m[1,0]
    near_value=array[x,y]

    return near_value

array =np.array([[60,200,30],[3,30,50],[20,1,-50],[20,-500,11]])
print(array)
value = 0
print(find_nearest(array, value))
