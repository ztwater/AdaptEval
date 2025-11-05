cmap = get_cmap(len(data))
for i, (X, Y) in enumerate(data):
   scatter(X, Y, c=cmap(i))
