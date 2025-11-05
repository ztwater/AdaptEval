# plot the data
with plt.style.context("bmh"):
    g = sns.catplot(
        kind="box",
        data=df,
        x="y", y="x"
    )
    ax = g.axes.flat[0]
    sns.stripplot(
        data=df,
        x="y", y="x",
        ax=ax, color='k',
        alpha=.25
    )
    plt.show()
