 demo = {'set1':{'t1':[1,2,3],'t2':[4,5,6],'t3':[7,8,9]}, 'set2':{'t1':[1,2,3],'t2':[4,5,6],'t3':[7,8,9]}, 'set3': {'t1':[1,2,3],'t2':[4,5,6],'t3':[7,8,9]}}
 df = pd.DataFrame.from_dict(demo, orient='index') 

 print(df.head())
 my_list=[]
 df2=pd.DataFrame(columns=['set','t1','t2','t3'])

 for key,item in df.iterrows():
    t1=item.t1
    t2=item.t2
    t3=item.t3
    mat1=np.matrix([t1,t2,t3])
    row1=[key,mat1[0,0],mat1[0,1],mat1[0,2]]
    df2.loc[len(df2)]=row1
    row2=[key,mat1[1,0],mat1[1,1],mat1[1,2]]
    df2.loc[len(df2)]=row2
    row3=[key,mat1[2,0],mat1[2,1],mat1[2,2]]
    df2.loc[len(df2)]=row3

print(df2) 

set t1 t2 t3
0  set1  1  2  3
1  set1  4  5  6
2  set1  7  8  9
3  set2  1  2  3
4  set2  4  5  6
5  set2  7  8  9
6  set3  1  2  3
7  set3  4  5  6
8  set3  7  8  9   
