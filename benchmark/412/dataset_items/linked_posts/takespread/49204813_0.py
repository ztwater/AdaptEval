which_idxs = lambda m, n: np.rint( np.linspace( 1, n, min(m,n) ) - 1 ).astype(int)

evenly_spaced = np.array( your_list )[which_idxs(m,n)]
