df = pd.DataFrame({
    "y": np.concatenate(( np.repeat(0, N0) , np.repeat(1, N1) )),
    "x": np.concatenate(( rvs0             , rvs1             )),
})
