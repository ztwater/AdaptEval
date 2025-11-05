# create a random dataset
rvs0 = dist0.rvs(N0, random_state=0)
rvs1 = dist1.rvs(N1, random_state=1)

with plt.style.context("bmh"):
    plt.hist(rvs0, alpha=.5, label="NEG")
    plt.hist(rvs1, alpha=.5, label="POS")
    plt.legend()
    plt.title("Random dataset")
