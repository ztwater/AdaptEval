import matplotlib.pyplot as plt

N = 16
cmap = cmap = plt.cm.get_cmap('gist_rainbow', N)

fig, axs = plt.subplots(2)
for ax in axs:
    ax.set_xlim([ 0, N])
    ax.set_ylim([-0.5, 0.5])
    ax.set_yticks([])

for i in range(0,N+1):
    v = int(calc(i, max = N))
    rect0 = plt.Rectangle((i, -0.5), 1, 1, facecolor=cmap(i))
    rect1 = plt.Rectangle((i, -0.5), 1, 1, facecolor=cmap(v))
    axs[0].add_artist(rect0)
    axs[1].add_artist(rect1)

plt.xticks(range(0, N), [int(calc(i, N)) for i in range(0, N)])
plt.show()
