# make a df with duplicate columns 'x'
df = pd.DataFrame({'x': range(5) , 'x':range(5), 'y':range(6, 11)}, columns = ['x', 'x', 'y']) 


df
Out[495]: 
   x  x   y
0  0  0   6
1  1  1   7
2  2  2   8
3  3  3   9
4  4  4  10

# attempting to drop the first column according to the solution offered so far     
df.drop(df.columns[0], axis = 1) 
   y
0  6
1  7
2  8
3  9
4  10
