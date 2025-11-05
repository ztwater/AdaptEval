n=20
for i,(x,y) in enumerate(points):
    plt.scatter(x, y, c=cmap(n*i))
