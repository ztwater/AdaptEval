df = df.explode('A')
df = df.explode('B')
df = df.drop_duplicates()
