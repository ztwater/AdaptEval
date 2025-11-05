def time_it():

    # initial values
    d = 20
    center, radius = np.full(d, 2), 3
    n_samples_list = np.logspace(3, 6, num=10).astype(int)
    runtime_my_code, runtime_daniel_code = [], []

    for n_samples in n_samples_list:

        # time my code
        start = time.perf_counter()
        sample_hypersphere_uniformly(center, radius, n_samples)
        end = time.perf_counter()
        duration = end - start
        runtime_my_code.append(duration)

        # time Daniel's code
        start = time.perf_counter()
        daniels_code(center, radius, n_samples)
        end = time.perf_counter()
        duration = end - start
        runtime_daniel_code.append(duration)

    # plot the results
    fig, ax = plt.subplots()
    ax.scatter(n_samples_list, runtime_my_code)
    ax.scatter(n_samples_list, runtime_daniel_code)
    ax.plot(n_samples_list, runtime_my_code, label='my code')
    ax.plot(n_samples_list, runtime_daniel_code, label='daniel\'s code')
    ax.set(xlabel='n_samples',
        ylabel='runtime (s)', title='runtime VS n_samples')
    plt.legend()
    fig.savefig('runtime_vs_n_samples.png')
