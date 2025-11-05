import matplotlib.pyplot as plt

N = len(data)
cmap = plt.cm.get_cmap("hsv", N+1)
for i in range(N):
    X,Y = data[i]
    plt.scatter(X, Y, c=cmap(i))
