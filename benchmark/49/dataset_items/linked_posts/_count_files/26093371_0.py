import os

total_con=os.listdir('<directory path>')

files=[]

for f_n in total_con:
   if os.path.isfile(f_n):
     files.append(f_n)


print len(files)
