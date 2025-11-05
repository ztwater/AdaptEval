def unnesting(df, explode, axis):
    if axis==1:
        df1 = pd.concat([df[x].explode() for x in explode], axis=1)
        return df1.join(df.drop(explode, 1), how='left')
    else :
        df1 = pd.concat([
                         pd.DataFrame(df[x].tolist(), index=df.index).add_prefix(x) for x in explode], axis=1)
        return df1.join(df.drop(explode, 1), how='left')
