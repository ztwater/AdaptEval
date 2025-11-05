l=[]
corr_matrix = df.corr().abs()

for ci in corr_matrix.columns: 
    for cj in corr_matrix.columns: 
        if (corr_matrix[ci][cj]>0.8 and ci!=cj):
            l.append(ci)
            
l = np.array(l)
to_drop = np.unique(l)
df.drop(to_drop, axis=1, inplace=True)
