def unnesting(var_0, var_1, var_2):
    if var_2==1:
        var_3 = pd.concat([var_0[x].explode() for x in var_1], var_2=1)
        return var_3.join(var_0.drop(var_1, 1), how='left')
    else :
        var_3 = pd.concat([
                         pd.DataFrame(df[x].tolist(), index=df.index).add_prefix(x) for x in var_1], var_2=1)
        return var_3.join(var_0.drop(var_1, 1), how='left')
