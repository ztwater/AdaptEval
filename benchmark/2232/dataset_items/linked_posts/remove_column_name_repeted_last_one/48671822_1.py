column_numbers = [x for x in range(df.shape[1])]  # list of columns' integer indices

column_numbers .remove(0) #removing column integer index 0
df.iloc[:, column_numbers] #return all columns except the 0th column

   x  y
0  0  6
1  1  7
2  2  8
3  3  9
4  4  10
