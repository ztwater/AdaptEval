which_idxs = lambda m, n: [idx for idx in np.rint( np.linspace( 1-n/(2*min(m,n)), n+n/(2*min(m,n)), min(m,n)+2 ) - 1 ).astype(int) if idx in range(n)]

evenly_spaced = np.array( your_list )[which_idxs(m,n)]
