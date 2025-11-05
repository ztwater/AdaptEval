row_index = 0
corrDict = {}
row_name = []
col_name = []
corr_val = []

while row_index < len(df.corr().index.tolist()):
    for index, x in enumerate(df.corr().iloc[row_index, :]):
        if abs(x) >= 0.8 and index != row_index:
            if abs(x) in corr_val:
                if (df.corr().index.tolist()[row_index] in col_name) and (df.corr().columns.tolist()[index] in row_name):
                    continue
            row_name.append(df.corr().index.tolist()[row_index])
            col_name.append(df.corr().columns.tolist()[index])
            corr_val.append(x)
    row_index += 1
    
corrDict ={"First Feature (FF)": row_name, "Second Feature (SF)": col_name, "Correlation (FF x SF)": corr_val}
corr_df2=pd.DataFrame(corrDict)
corr_df2
