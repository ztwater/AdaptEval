items = [
    ["1", ["a", "b", "c"]],
    ["2", ["d", "e", "f"]]
]

df = pd.DataFrame(items, columns = ["col1", "col2"])
print(df)

t = horizontal_explode(df=df, col_name="col2")
del t["col2"]
print(t)

t = horizontal_explode(df=df, col_name="col2", new_columns=["new_col1", "new_col2", "new_col3"])
del t["col2"]
print(t)
