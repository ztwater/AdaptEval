# generate random colors
colors_ = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# how many random colors to generate?
colors = colors_(6)
for i,color in zip(range(1, 7), colors):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
           fontsize=18, ha='center', color=color)
