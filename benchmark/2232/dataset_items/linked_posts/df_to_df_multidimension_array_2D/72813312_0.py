ggg = pd.DataFrame({"a":[1,2,3,4,5,6,7], "b":[7,6,5,4,3,2,1]})

def my_rolling_apply2(df, fun, window):
    prepend = [None] * (window - 1)
    end = len(df) - window
    mid = map(lambda start: fun(df[start:start + window]), np.arange(0,end))
    last =  fun(df[end:])
    return [*prepend, *mid, last]

my_rolling_apply2(ggg, lambda df: (df["a"].max(), df["b"].min()), 3)
