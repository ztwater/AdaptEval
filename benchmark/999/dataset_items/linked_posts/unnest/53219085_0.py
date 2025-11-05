df=pd.concat([df]*2).sort_index()
it=iter(df['B'].tolist()[0]+df['B'].tolist()[0])
df['B']=df['B'].apply(lambda x:next(it))
