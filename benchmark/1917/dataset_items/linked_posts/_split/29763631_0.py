import numpy as np   
a=np.arange(10)
print "Input array:",a 
parts=3
i=np.linspace(np.min(a),np.max(a)+1,parts+1)
i=np.array(i,dtype='uint16') # Indices should be floats
split_arr=[]
for ind in range(i.size-1):
    split_arr.append(a[i[ind]:i[ind+1]]
print "Array split in to %d parts : "%(parts),split_arr
