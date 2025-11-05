# Here's the answer to the related question in:
# https://stackoverflow.com/q/56708671/11426125

# initial dataframe
df12=pd.DataFrame({'Date':['2007-12-03','2008-09-07'],'names':
[['Peter','Alex'],['Donald','Stan']]})

# convert dataframe to array for indexing list values (names)
a = np.array(df12.values)  

# create a new, dataframe with dimensions for unnested
b = np.ndarray(shape = (4,2))
df2 = pd.DataFrame(b, columns = ["Date", "names"], dtype = str)

# implement loops to assign date/name values as required
i = range(len(a[0]))
j = range(len(a[0]))
for x in i:
    for y in j:
        df2.iat[2*x+y, 0] = a[x][0]
        df2.iat[2*x+y, 1] = a[x][1][y]

# set Date column as Index
df2.Date=pd.to_datetime(df2.Date)
df2.index=df2.Date
df2.drop('Date',axis=1,inplace =True)
